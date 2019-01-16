
import unittest

import numpy as np
from sklearn.linear_model import Ridge
from tfnumpy.regression import fit_linear_regression


class LinearRegressionTester(unittest.TestCase):
    def setUp(self):
        self.xtrain = np.array([[0.], [1.], [2.], [3.]])
        self.ytrain = np.array([[-1.199071], [1.098184], [3.399706], [5.700929]])

    def tearDown(self):
        pass

    def test_regression(self):
        regressed_results, tfsess = fit_linear_regression(self.xtrain, self.ytrain, max_iter=2000)

        # check regression coefficients
        self.assertEqual(regressed_results['nbfeatures'], 1)
        self.assertEqual(regressed_results['nbtrain'], 4)
        self.assertAlmostEqual(regressed_results['theta'][0], 2.30, 2)
        self.assertAlmostEqual(regressed_results['b'], -1.20, 2)

        # check prediction
        self.assertAlmostEqual(tfsess['session'].run(tfsess['outputs'], feed_dict={tfsess['inputs']: np.array([[1]])})[0][0],
                               1.1006711, 4)
        self.assertAlmostEqual(tfsess['session'].run(tfsess['outputs'], feed_dict={tfsess['inputs']: np.array([[2.5]])})[0][0],
                               4.549828400000001, 4)

    def test_ridge(self):
        ridge_reg = Ridge(alpha=0.1, solver='cholesky')
        ridge_reg.fit(self.xtrain, self.ytrain)

        tfnp_reg, tfsess = fit_linear_regression(self.xtrain, self.ytrain, max_iter=2000, ridge_alpha=0.1)

        # check sklearn results
        self.assertAlmostEqual(ridge_reg.predict([[1]])[0][0], 1.12241141, 2)
        self.assertAlmostEqual(ridge_reg.predict([[2.5]])[0][0], 4.50498818, 2)

        # check tensorflow prediction
        self.assertAlmostEqual(tfsess['session'].run(tfsess['outputs'], feed_dict={tfsess['inputs']: np.array([[1]])})[0][0],
                               1.220062, 2)
        self.assertAlmostEqual(tfsess['session'].run(tfsess['outputs'], feed_dict={tfsess['inputs']: np.array([[2.5]])})[0][0],
                               4.4537644, 2)


    def test_lasso(self):
        pass

    def test_both(self):
        pass



if __name__ == '__main__':
    unittest.main()