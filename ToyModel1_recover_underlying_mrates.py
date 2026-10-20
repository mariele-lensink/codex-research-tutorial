"""Synthetic discovery demo: tissue environments change mutation rates."""
import argparse
import csv
import json
import os
from pathlib import Path
import tempfile

# Keep plotting caches writable when running in a restricted workspace.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "toy-model-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np

BASELINE_RATE = 0.002
EXPOSURE_EFFECT = 0.003
SCENARIOS = {"Different environments": {"Liver": 0, "Colon": 1},
             "Equalized exposure": {"Liver": 0, "Colon": 0}}


def mutation_rate(exposure):
    # Both tissues have identical intrinsic biology in this toy world.
    return BASELINE_RATE + EXPOSURE_EFFECT * exposure


def simulate(seed=42, repeats=500, bins=100, opportunities=1000):
    if min(repeats, bins, opportunities) <= 0:
        raise ValueError("Repeats, bins, and opportunities must be positive")
    streams = np.random.SeedSequence(seed).spawn(4)
    results = {}
    for scenario, exposures in SCENARIOS.items():
        results[scenario] = {}
        for tissue, exposure in exposures.items():
            rng = np.random.default_rng(streams.pop(0))
            counts = rng.poisson(opportunities * mutation_rate(exposure),
                                 size=(repeats, bins))
            results[scenario][tissue] = counts.sum(axis=1) / (bins * opportunities)
    return results


def summarize(results):
    summary = {}
    for scenario, tissues in results.items():
        gap = tissues["Colon"] - tissues["Liver"]
        summary[scenario] = {
            "mean_rates": {t: float(x.mean()) for t, x in tissues.items()},
            "mean_colon_minus_liver": float(gap.mean()),
            "gap_simulation_interval_95": np.quantile(gap, [0.025, 0.975]).tolist(),
        }
    return summary


def plot(results, observations, output):
    fig, axes = plt.subplots(1, len(results), figsize=(6 * len(results), 4.5),
                             sharey=True, squeeze=False)
    for ax, (scenario, tissues) in zip(axes[0], results.items()):
        # Whiskers show the central 95% across simulated experiments, not a CI.
        boxes = ax.boxplot([x * 1000 for x in tissues.values()],
                           patch_artist=True, whis=(2.5, 97.5), showfliers=False)
        for box in boxes["boxes"]:
            box.set_facecolor("#4998bc")
            box.set_alpha(0.75)
        for median in boxes["medians"]:
            median.set_color("#173b50")
        if scenario in observations:
            ax.scatter([1, 2], [observations[scenario][t][0] * 1000 for t in tissues],
                       color="#e87924", marker="D", edgecolors="black", s=65, zorder=4)
        ax.set_xticks([1, 2], list(tissues))
        ax.axhline(BASELINE_RATE * 1000, color="gray", linestyle="--", linewidth=1)
        ax.set_title(scenario if scenario in observations
                     else scenario + "\nSimulated intervention only")
        ax.set_ylim(bottom=0)
        ax.grid(axis="y", alpha=0.2)
    axes[0, 0].set_ylabel("Estimated mutations per 1,000 callable opportunities")
    fig.suptitle("Synthetic tissue mutation rates", fontsize=15)
    fig.legend(handles=[Patch(facecolor="#4998bc", alpha=0.75, label="Model simulations (500 per group)"),
                        Line2D([], [], color="#e87924", marker="D", linestyle="None",
                               markeredgecolor="black", label="Fake observed data (one sample)")],
               loc="upper center", bbox_to_anchor=(0.5, 0.91), ncol=2, frameon=False,
               fontsize=9)
    fig.text(0.5, 0.015, "Both datasets are synthetic; observations use a separate random seed.\n"
             "Boxes: middle 50%; whiskers: central 95%. Exposure effect is assumed.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.10, 1, 0.85))
    fig.savefig(output, dpi=180)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=["observe", "test"], default="test")
    args = parser.parse_args()
    results = simulate()
    # Fake measurements exist only for the original tissue environments.
    observations = {"Different environments":
                    simulate(seed=2026, repeats=1)["Different environments"]}
    if args.stage == "observe":
        results = {"Different environments": results["Different environments"]}
    output = Path(__file__).resolve().parent / "figures"
    output.mkdir(exist_ok=True)
    name = "observed_rates" if args.stage == "observe" else "exposure_test"
    plot(results, observations, output / (name + ".png"))
    with (output / (name + "_observations.csv")).open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["scenario", "tissue", "fake_observed_rate_per_opportunity"])
        for scenario in observations:
            writer.writerows((scenario, tissue, rates[0])
                             for tissue, rates in observations[scenario].items())
    with (output / (name + ".csv")).open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["scenario", "replicate", "tissue", "estimated_rate_per_opportunity"])
        for scenario, tissues in results.items():
            for tissue, rates in tissues.items():
                writer.writerows((scenario, i, tissue, rate) for i, rate in enumerate(rates))
    report = {"data_source": "synthetic", "seed": 42, "repeats": 500,
              "fake_observation_seed": 2026,
              "fake_observations": {s: {t: float(x[0]) for t, x in observations[s].items()}
                                    for s in observations},
              "bins": 100, "opportunities_per_bin": 1000,
              "baseline_rate": BASELINE_RATE, "exposure_effect": EXPOSURE_EFFECT,
              "numpy_version": np.__version__, "matplotlib_version": matplotlib.__version__,
              "results": summarize(results)}
    (output / (name + ".json")).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    print("Figure:", output / (name + ".png"))


if __name__ == "__main__":
    main()
