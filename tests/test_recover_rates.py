import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from recover_rates import estimate_rate, simulate


class EstimationTests(unittest.TestCase):
    def test_known_counts(self):
        self.assertEqual(estimate_rate([2, 4], [1000, 1000]), 0.003)
        self.assertEqual(estimate_rate([0, 0], [100, 100]), 0)

    def test_unequal_opportunities_use_pooled_exposure(self):
        self.assertAlmostEqual(estimate_rate([1, 9], [100, 300]), 0.025)

    def test_invalid_data_rejected(self):
        for counts, exposure in [([], []), ([1], [0]), ([-1], [10]),
                                 ([1.5], [10]), ([1, 2], [10]),
                                 ([float("nan")], [10])]:
            with self.assertRaises(ValueError):
                estimate_rate(counts, exposure)

    def test_seed_reproduces_experiment(self):
        self.assertEqual(simulate(42, 100, 1000), simulate(42, 100, 1000))

    def test_invalid_design_rejected(self):
        with self.assertRaises(ValueError):
            simulate(42, 0, 1000)


if __name__ == "__main__":
    unittest.main()
