"""Distinguish tissue and exposure effects using synthetic held-out samples."""
import argparse
import csv
import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "toy-model-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.optimize import minimize
from scipy.special import xlogy

MODELS = {"tissue_only": (True, False), "exposure_only": (False, True),
          "combined": (True, True)}
DTYPE = [("sample", int), ("skin", int), ("exposure", float),
         ("opportunities", int), ("count", int)]


def generate(seed, samples_per_cell=20, opportunities=10000,
             baseline=0.002, tissue_effect=0.001, exposure_effect=0.003):
    """Generator parameters are teaching assumptions, never inputs to fitting."""
    if samples_per_cell <= 0 or opportunities <= 0:
        raise ValueError("Sample size and opportunities must be positive")
    if min(baseline, tissue_effect, exposure_effect) < 0:
        raise ValueError("Generator rates/effects must be nonnegative")
    rng = np.random.default_rng(seed)
    rows = []
    for skin in (0, 1):
        for exposure in np.linspace(0, 1, 5):
            rate = baseline + tissue_effect * skin + exposure_effect * exposure
            for _ in range(samples_per_cell):
                rows.append((len(rows), skin, exposure, opportunities,
                             rng.poisson(opportunities * rate)))
    return np.array(rows, dtype=DTYPE)


def design(data, model):
    tissue, exposure = MODELS[model]
    columns = [np.ones(len(data))]
    if tissue:
        columns.append(data["skin"])
    if exposure:
        columns.append(data["exposure"])
    return np.column_stack(columns)


def fit(data, model):
    """Fit nonnegative additive rates by training Poisson likelihood.

    Coefficients use rates per 1,000 opportunities for numerical stability.
    Nonnegative effects are an explicit restriction of these candidate models.
    """
    x = design(data, model)
    if np.linalg.matrix_rank(x) < x.shape[1]:
        raise ValueError("Design cannot distinguish the requested effects")
    scale = data["opportunities"] / 1000
    y = data["count"]

    def objective(beta):
        mu = scale * np.sum(x * beta, axis=1)
        loss = np.sum(mu - xlogy(y, mu))
        gradient = np.sum(x * (scale * (1 - y / mu))[:, None], axis=0)
        return loss, gradient

    start = np.full(x.shape[1], 0.1)
    start[0] = max(float(y.sum() / scale.sum()), 0.001)
    bounds = [(1e-9, None)] + [(0, None)] * (len(start) - 1)
    result = minimize(objective, start, jac=True, bounds=bounds,
                      method="L-BFGS-B", options={"ftol": 1e-12, "gtol": 1e-7})
    if not result.success:
        raise RuntimeError(f"{model} fit failed: {result.message}")
    return result.x


def predict(data, model, coefficients):
    return np.sum(design(data, model) * coefficients, axis=1) / 1000


def poisson_deviance(counts, expected):
    """Mean held-out Poisson deviance per sample; lower is better."""
    if np.any(expected <= 0):
        raise ValueError("Expected counts must be positive")
    return float(np.mean(2 * (xlogy(counts, counts / expected) - counts + expected)))


def compare(training, heldout):
    results = {}
    for model in MODELS:
        beta = fit(training, model)
        expected = heldout["opportunities"] * predict(heldout, model, beta)
        names = ["baseline"]
        if MODELS[model][0]:
            names.append("skin_effect")
        if MODELS[model][1]:
            names.append("exposure_effect")
        results[model] = {
            "coefficients_per_opportunity": dict(zip(names, (beta / 1000).tolist())),
            "heldout_mean_poisson_deviance": poisson_deviance(heldout["count"], expected),
        }
    return results


def save_data(path, data):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(data.dtype.names)
        writer.writerows(data.tolist())


def plot(data, output, results=None):
    fig, axes = plt.subplots(1, 2 if results else 1, figsize=(12 if results else 7, 4.5),
                             squeeze=False)
    ax = axes[0, 0]
    for skin, color, label in [(0, "#2878a5", "Liver"), (1, "#db7927", "Skin")]:
        group = data[data["skin"] == skin]
        ax.scatter(group["exposure"], 1000 * group["count"] / group["opportunities"],
                   alpha=0.25, color=color, label=label)
        if results:
            grid = np.zeros(100, dtype=DTYPE)
            grid["skin"] = skin
            grid["exposure"] = np.linspace(0, 1, 100)
            c = results["combined"]["coefficients_per_opportunity"]
            rates = c["baseline"] + skin * c["skin_effect"] + grid["exposure"] * c["exposure_effect"]
            ax.plot(grid["exposure"], rates * 1000, color=color)
    ax.set(xlabel="Exposure (synthetic units)", ylabel="Mutations per 1,000 opportunities",
           title="Held-out samples and fitted combined model" if results else "Training samples only")
    ax.legend()
    if results:
        score_ax = axes[0, 1]
        score_ax.bar(list(results), [r["heldout_mean_poisson_deviance"] for r in results.values()],
                     color="#4998bc")
        score_ax.set(ylabel="Mean Poisson deviance (lower is better)", title="Held-out prediction")
    fig.suptitle("Synthetic data: overlapping exposures in both tissues")
    fig.tight_layout()
    fig.savefig(output, dpi=180)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=["observe", "test"], default="observe")
    args = parser.parse_args()
    output = Path(__file__).resolve().parent / "figures"
    output.mkdir(exist_ok=True)
    training = generate(2026)
    save_data(output / "inference_training.csv", training)
    report = {"data_source": "synthetic", "training_seed": 2026,
              "samples_per_tissue_exposure_cell_per_split": 20,
              "exposure_levels": [0, 0.25, 0.5, 0.75, 1], "opportunities_per_sample": 10000,
              "numpy_version": np.__version__, "scipy_version": scipy.__version__,
              "matplotlib_version": matplotlib.__version__,
              "generator_parameters": {"baseline": 0.002, "tissue_effect": 0.001,
                                       "exposure_effect": 0.003}}
    prefix = "inference_observations"
    if args.stage == "test":
        heldout = generate(2027)
        results = compare(training, heldout)
        report.update(heldout_seed=2027, models=results,
                      fitting="Training-only Poisson likelihood; nonnegative additive effects",
                      scoring="Mean held-out Poisson deviance per sample; lower is better")
        save_data(output / "inference_heldout.csv", heldout)
        prefix = "inference_comparison"
        plot(heldout, output / (prefix + ".png"), results)
    else:
        plot(training, output / (prefix + ".png"))
    (output / (prefix + ".json")).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    print("Figure:", output / (prefix + ".png"))


if __name__ == "__main__":
    main()
