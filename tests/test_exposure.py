import unittest
import numpy as np
from ToyModel1_recover_underlying_mrates import (
    generate, design, fit, predict, compare, poisson_deviance,
)


class InferenceTests(unittest.TestCase):
    def test_reproducible_independent_splits_and_overlap(self):
        train, heldout = generate(2026), generate(2027)
        np.testing.assert_array_equal(train, generate(2026))
        self.assertFalse(np.array_equal(train['count'], heldout['count']))
        for skin in (0, 1):
            self.assertEqual(set(train['exposure'][train['skin'] == skin]),
                             {0, .25, .5, .75, 1})
        self.assertEqual(np.linalg.matrix_rank(design(train, 'combined')), 3)

    def test_recovers_both_effects_with_ample_data(self):
        data = generate(7, samples_per_cell=200, opportunities=100000)
        np.testing.assert_allclose(fit(data, 'combined') / 1000,
                                   [.002, .001, .003], atol=.00005, rtol=0)

    def test_heldout_counts_do_not_change_fitted_parameters(self):
        training, heldout = generate(2026), generate(2027)
        first = compare(training, heldout)
        heldout['count'] += 10
        second = compare(training, heldout)
        for name in first:
            self.assertEqual(first[name]['coefficients_per_opportunity'],
                             second[name]['coefficients_per_opportunity'])
            self.assertNotEqual(first[name]['heldout_mean_poisson_deviance'],
                                second[name]['heldout_mean_poisson_deviance'])

    def test_signal_ablation_changes_preferred_model(self):
        # Omitted effects harm prediction when a strong signal is present.
        for tissue, exposure, omitted in [(0.003, 0, 'exposure_only'),
                                         (0, 0.004, 'tissue_only')]:
            train = generate(11, tissue_effect=tissue, exposure_effect=exposure)
            test = generate(12, tissue_effect=tissue, exposure_effect=exposure)
            result = compare(train, test)
            self.assertLess(result['combined']['heldout_mean_poisson_deviance'],
                            result[omitted]['heldout_mean_poisson_deviance'])

    def test_deviance_zero_counts_and_unidentifiable_design(self):
        self.assertAlmostEqual(poisson_deviance(np.array([0, 2]), np.array([1, 2])), 1)
        data = generate(1)
        data['exposure'] = data['skin']
        with self.assertRaisesRegex(ValueError, 'cannot distinguish'):
            fit(data, 'combined')
        self.assertTrue(np.all(predict(generate(2), 'combined', np.array([2, 1, 3])) > 0))


if __name__ == '__main__':
    unittest.main()
