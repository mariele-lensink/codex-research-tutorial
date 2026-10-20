import unittest
import numpy as np
from ToyModel1_recover_underlying_mrates import mutation_rate, simulate, summarize


class ExposureExperimentTests(unittest.TestCase):
    def test_equal_environment_removes_expected_tissue_difference(self):
        self.assertEqual(mutation_rate(0), 0.002)
        self.assertAlmostEqual(mutation_rate(1) - mutation_rate(0), 0.003)

    def test_repeated_experiments_recover_imposed_effect(self):
        results = simulate()
        summary = summarize(results)
        natural = summary['Different environments']['mean_colon_minus_liver']
        control = summary['Equalized exposure']['mean_colon_minus_liver']
        # Conservative Monte Carlo tolerances, far smaller than the .003 effect.
        self.assertAlmostEqual(natural, 0.003, delta=0.0001)
        self.assertAlmostEqual(control, 0, delta=0.0001)

    def test_seed_reproduces_data(self):
        first, second = simulate(repeats=5), simulate(repeats=5)
        for scenario in first:
            for tissue in first[scenario]:
                np.testing.assert_array_equal(first[scenario][tissue], second[scenario][tissue])


if __name__ == '__main__':
    unittest.main()
