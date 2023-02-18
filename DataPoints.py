import pandas as pd
import math
from Line import Line
import numpy as np
from functools import reduce

class DataPoints:
    def __init__(self, df):
        self.df = df
        self.n = df.shape[0]

    def bestLine(self, i = 0, j = None):
        j = None if j is None else self.n
        (x, y) = (np.array(self.df['x'].iloc[i:j]), np.array(self.df['y'].iloc[i:j]))
        a = (self.n * x @ y - sum(x) * sum(y)) / (self.n * x @ x - sum(x) * sum(x))
        b = (sum(y) - a * sum(x)) / self.n
        return Line(a = a, b = b)

    def error(self, i = 0, j = None):
        j = None if j is None else self.n
        if i >= j:
            return 0
        else:
            L = self.bestLine(i, j)
            fitted = L.fitPoints(self.df['x'].iloc[i:j])
            resids = np.array(self.df['y'].iloc[i:j] - fitted['y'])
            return resids @ resids

    def errorMatrix(self):
        return np.fromfunction(self.error, shape = (self.n, self.n), dtype = float)

    def segmentedLeastSquares(self, cost):
        em = self.errorMatrix()
        optError = np.zeros(self.n)
        for j in range(1, self.n):
            optError[j] = min(pd.Series(range(j + 1)).map(lambda i: self.error(i, j) + cost + optError[i - 1]))


