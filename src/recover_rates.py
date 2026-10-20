"""Recover per-opportunity mutation rates from synthetic Poisson counts."""
import argparse
import json
from pathlib import Path
import numpy as np

TRUE_RATES = {"liver": 0.002, "colon": 0.005}


def estimate_rate(counts, opportunities):
    counts = np.asarray(counts, dtype=float)
    opportunities = np.asarray(opportunities, dtype=float)
    if counts.ndim != 1 or counts.size == 0 or counts.shape != opportunities.shape:
        raise ValueError("counts and opportunities must be nonempty matching vectors")
    if not np.all(np.isfinite(counts)) or np.any(counts < 0) or np.any(counts != np.floor(counts)):
        raise ValueError("counts must be finite nonnegative integers")
    if not np.all(np.isfinite(opportunities)) or np.any(opportunities <= 0):
        raise ValueError("opportunities must be finite and positive")
    return float(counts.sum() / opportunities.sum())


def simulate(seed, bins, opportunities_per_bin):
    if bins <= 0 or opportunities_per_bin <= 0 or not np.isfinite(opportunities_per_bin):
        raise ValueError("bins and opportunities_per_bin must be positive and finite")
    rng = np.random.default_rng(seed)
    opportunities = np.full(bins, opportunities_per_bin)
    tissues = {}
    for tissue, rate in TRUE_RATES.items():
        counts = rng.poisson(opportunities * rate)
        estimate = estimate_rate(counts, opportunities)
        tissues[tissue] = {
            "true_rate_per_opportunity": rate,
            "first_10_counts": counts[:10].tolist(),
            "total_counts": int(counts.sum()),
            "mean_count_per_bin": float(counts.mean()),
            "estimated_rate_per_opportunity": estimate,
            "absolute_error": abs(estimate - rate),
        }
    return {"seed": seed, "bins_per_tissue": bins,
            "opportunities_per_bin": opportunities_per_bin,
            "numpy_version": np.__version__,
            "data_source": "synthetic independent Poisson counts",
            "tissues": tissues}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--bins", type=int, default=100)
    parser.add_argument("--opportunities-per-bin", type=int, default=1000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.bins <= 0 or args.opportunities_per_bin <= 0:
        parser.error("--bins and --opportunities-per-bin must be positive")
    report = json.dumps(simulate(args.seed, args.bins, args.opportunities_per_bin), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    print(report, end="")


if __name__ == "__main__":
    main()
