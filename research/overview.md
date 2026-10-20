# Recovering underlying mutation rates

Adapted from the researcher's saved `../ToyModel1_recover_underlying_mrates.py`.
The original file is preserved. Its liver draw reads `rng. L * r_liver`, which
attempts an RNG attribute lookup. The tutorial uses `rng.poisson(mu_liver)`.

Question: can we recover known tissue mutation rates from observed counts and
callable opportunities, and how does available exposure affect recovery?

Model: Y_i ~ Poisson(L_i * r), independently across bins and tissues.
Baseline: 100 bins per tissue, 1000 opportunities per bin, liver r=0.002,
colon r=0.005, NumPy default_rng seed 42. Expected counts per bin are 2 and 5.
Estimate r as sum(Y_i) / sum(L_i). This handles unequal opportunity counts;
mean(counts) alone has units of mutations per bin, not mutations per opportunity.

Assumptions: constant rate within each tissue, known callable opportunities,
independent Poisson counts, and no extra observation bias or overdispersion.
These are synthetic data, not empirical evidence about tissue mutation rates.

Baseline: `python3 src/recover_rates.py --seed 42 --bins 100 --opportunities-per-bin 1000`

Next hypothesis to record before comparison: more total opportunities should
reduce average estimation error over repeated simulations, though individual
runs need not improve. Compare 10, 100, and 1000 bins at 1000 opportunities/bin
over seeds 0 through 29; summarize errors and variability by tissue.
