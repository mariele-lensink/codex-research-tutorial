# Research demo: tissue environments and mutation rates

Open this folder as the project workspace. Follow **DEMO_SCRIPT.md** for the
spoken narrative and copyable main-chat prompts, including both agent handoffs.

The toy world gives both tissues the same intrinsic mutation rate (0.002 per
callable opportunity). Skin's original environment represents greater mutagenic exposure (motivated
by sunlight/UV) and adds an illustrative exposure effect
of 0.003. Equalizing exposure removes that imposed difference in expectation.
We compare 500 synthetic experiments per scenario, each with 100 bins and
1000 callable opportunities per bin; seed 42 initializes four child RNG streams.
The initial rate difference alone cannot identify exposure as its cause.
This demo tests an assumed mechanism, not a causal claim about real tissue.

Install requirements in your Python environment, then run:

```sh
python3 ToyModel1_recover_underlying_mrates.py --stage observe
python3 ToyModel1_recover_underlying_mrates.py --stage test
python3 -m unittest discover -s tests -v
```

`figures/observed_rates.png` shows the original environments;
`figures/exposure_test.png` adds the equalized-exposure intervention.
Orange diamonds are fake observed data for the original environments only
(one independent sample per tissue, seed 2026); blue boxes are the 500 model
simulations (seed 42). Equalized exposure is a simulated intervention with no
observed measurements. Both data sources are
synthetic draws from the same assumed mechanism, not independent biological
validation. Fake observations are saved separately in `*_observations.csv`
and in each JSON summary; the original CSV files contain model simulations.
Each has a CSV of replicate rate estimates and a JSON summary containing
parameters, package versions, mean rates, and skin-minus-liver differences.
Figure whiskers and JSON intervals describe central 95% simulation variability,
not confidence intervals for the mean. Outputs are absent from the setup
checkpoint; the commands above regenerate them for review and a results commit.

- `ToyModel1_recover_underlying_mrates.py`: simulation, summaries, and figures.
- `lab_notebook.txt`: dated plans, actual outcomes, and limitations.
- `.codex/agents/`: active lab_notebook and git_steward definitions.
- `AGENTS.md`: proactive main-chat delegation workflow.
- `GIT_CHECKPOINT.md`: steward's final review and publication prompts.

The earlier tutorial remains accessible in Git history at `c84e528`; no archive
directory is present in this setup.

Agents act when invoked during active chat work. The notebook is updated before
final steward review. Git commits and publication follow explicit authorization.
The existing repository history and remote remain in place.
