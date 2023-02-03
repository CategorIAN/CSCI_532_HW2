import numpy as np
import math
from functools import reduce
from cmath import *
import pandas as pd
from copy import copy

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.deg = len(coeffs) - 1

    def __str__(self):
        return str(self.coeffs)

    def __call__(self, x):
        return reduce(lambda r, a: r * x + a, self.coeffs[1:], self.coeffs[0])

    def rou(self, n, k = 1):
        return pow(exp(complex(0, 2 * pi / n)), k)

    def even(self):
        if self.deg % 2 == 0:
            return Polynomial([self.coeffs[2 * i] for i in range(self.deg // 2 + 1)])
        else:
            return Polynomial([self.coeffs[2 * i + 1] for i in range(self.deg // 2 + 1)])

    def odd(self):
        if self.deg % 2 == 0:
            return Polynomial([self.coeffs[2 * i + 1] for i in range(self.deg // 2)])
        else:
            return Polynomial([self.coeffs[2 * i] for i in range(self.deg // 2 + 1)])


    def DFT(self, inv = False):
        size = 1
        n = self.deg + 1
        while size < n:
            size = size * 2
        padded = copy(self.coeffs)
        while n < size:
            padded = [0] + padded
            n += 1
        P = Polynomial(padded)
        return np.vectorize(P.fast_eval(inv))(np.array(range(P.deg + 1)))

    def invDFT(self):
        pass

    def fast_eval(self, inv, k):
        n = self.deg
        def go(P, j):
            if P.deg < 4:
                if inv:
                    return self(self.rou(n, -k)) / n
                else:
                    return self(self.rou(n, k))
            else:
                return self.even().fast_eval(inv)(2 * k) + self.rou(n, (1 - 2 * int(inv)) * k) * self.odd().fast_eval(2 * k)
        return f

    def fast_multiply(self, Q):
        fourier_prod = self.DFT() * Q.DFT()






