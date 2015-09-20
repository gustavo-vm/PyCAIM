__author__ = 'morgan'
import unittest
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
from pandas.util.testing import assert_series_equal
from caime import CAIM

# Expected DiscreteData and QuantaMatrix
DI_res =[
    ([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [[1, 10], [0, 9], [0, 13]]),
    ([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [[1, 10], [0, 9], [1, 12]]),
    ([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [[2, 9],[0, 9],[1, 12]]),
    ([0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [[3, 8], [0, 9], [1, 12]]),
    ([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[5, 6, 0], [1, 4, 4], [2, 4, 7]]),
    ([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[6, 5, 0], [1, 4, 4], [3, 3, 7]]),
    ([0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[6, 5, 0], [1, 4, 4], [4, 2, 7]]),
    ([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[6, 5, 0], [2, 3, 4], [4, 2, 7]]),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[6, 5, 0], [2, 3, 4], [5, 1, 7]]),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[7, 4, 0], [3, 2, 4], [5, 1, 7]]),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[7, 4, 0], [5, 0, 4], [6, 0, 7]]),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,2,2,2], [[8, 3, 0], [5, 0,  4], [6, 0, 7]]),
    ([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3], [[1, 10, 0, 0], [0,  5, 3, 1], [0,  6, 7, 0]]),
    ([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4], [[1, 6, 4, 0, 0], [0, 5, 0, 3, 1], [0, 6, 0, 7, 0]]),
    ([0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5], [[1, 5, 1, 4, 0, 0], [0, 1, 4, 0, 3, 1], [0, 3, 3, 0, 7, 0]])
]

# Discrete Interval inputs to discrete_with_interval
DI = [
      [0.05],
      [0.15],
      [0.25],
      [0.35],
      [0.55000, 1.35000],
      [0.65000, 1.35000],
      [0.75000, 1.35000],
      [0.85000, 1.35000],
      [0.95000, 1.35000],
      [1.0500, 1.3500],
      [1.1500, 1.3500],
      [1.2500, 1.3500],
      [0.050000, 1.350000, 2.050000],
      [0.050000, 1.150000, 1.350000, 2.050000],
      [0.050000, 0.650000, 1.150000, 1.350000, 2.050000]]


CE_input = [
    [1.85000,   0.00000,   0.00000, 0.0, 0.0],
    [0.35000,   1.35000,   0.00000, 0.0, 0.0],
    [0.050000,   1.350000,   2.050000, 0.0, 0.0],
    [1.3500,   1.7500,   2.0500, 0.0, 0.0],
    [0.050000,   1.150000,   1.350000,  2.050000, 0.0],
    [0.050000,   0.650000,   1.150000,  1.350000,  2.050000],
]

CE_res = [
    4.0333, 2.0167, 1.3444, 1.0083, 0.80667, 2.2500, 2.9028, 1.9352, 1.4514,
    1.1611, 1, 2.8810, 3.5540, 2.6655, 2.1324, 5.5000, 3.8929, 3.5952, 2.6964,
    2.1571, 1, 1.5588, 2.3725, 3.0044, 2.4035, 1, 1.8889, 1.9259, 2.4444, 2.9356,
]

discret_data_res_dict = {
    'F0': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 2.0, 19: 2.0, 20: 2.0, 21: 2.0, 22: 3.0, 23: 3.0, 24: 3.0, 25: 3.0, 26: 3.0, 27: 3.0, 28: 3.0, 29: 3.0, 30: 3.0, 31: 3.0, 32: 4.0},
    'C0': {0: 1.0, 1: 0.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0.0, 6: 1.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 1.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 0.0, 23: 0.0, 24: 0.0, 25: 0.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.0, 31: 0.0, 32: 0.0},
    'C1': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 1.0, 12: 0.0, 13: 0.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0, 25: 0.0, 26: 1.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 0.0, 31: 0.0, 32: 1.0},
    'C2': {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 1.0, 8: 0.0, 9: 1.0, 10: 1.0, 11: 0.0, 12: 1.0, 13: 0.0, 14: 0.0, 15: 1.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 1.0, 30: 1.0, 31: 1.0, 32: 0.0}}

cols = ['F0', 'C0', 'C1', 'C2']
discret_data_res = pd.DataFrame(discret_data_res_dict)[cols]
discretization_set_res = pd.DataFrame({0:[0.65, 1.15, 1.35, 2.05]})

discretization_set_res.astype(float)

class TestCAIM(unittest.TestCase):
    input_df = pd.read_csv('test_data.csv')
    X = input_df[['F0']]
    Y = input_df[['F0', 'C1', 'C2']]

    def test_discrete_with_interval(self):
        DI_test = list(zip(DI, DI_res))
        column = 0
        c = 3

        for i, di in enumerate(DI_test):
            data, quanta = CAIM.discrete_with_interval(self.input_df,#self.OriginalData,
                                                       c, column,
                                                       pd.Series(di[0]))
            self.assertTrue(np.array_equal(np.array(di[1][0]), data))
            self.assertTrue(np.array_equal(np.array(di[1][1]), quanta))

    def test_caim_eval(self):

        dtemp_test = []
        j = 0
        for input in CE_input:
            for k in range(1, len(input) + 1):
                dtemp_test.append( (pd.Series(input[:k]),
                                    CE_res[j]))
                j+=1

        c = 3
        column = 0
        for dtemp_t in dtemp_test:
            eval_in = dtemp_t[0]
            eval_expected = dtemp_t[1]
            val = CAIM.CAIM_eval(self.input_df,
                                 c, column, eval_in)
            #print("Val: %f  --  Expected: %f" %(val, eval_expected))
            assert np.isclose(val, eval_expected, atol=.001, rtol=.001)

    def test_fit_output(self):
        caim = CAIM().fit(self.input_df[['F0']],
                          self.input_df[['C0', 'C1', 'C2']])
        assert_frame_equal(caim.DiscreteData, discret_data_res)
        assert_frame_equal(caim.DiscretizationSet, discretization_set_res)

if __name__ == "__main__":
    unittest.main()
