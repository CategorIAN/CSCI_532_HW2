import pandas as pd
import math
from Line import Line

class DataPoints:
    def __init__(self, df):
        self.df = df
        self.x = df['x']
        self.y = df['y']
        self.n = df.shape[0]

    def bestLine(self):
        (xy, xx) = (self.x * self.y, self.x * self.x)
        a = (self.n * sum(xy) - sum(self.x) * sum(self.y)) / (self.n * sum(xx) - math.pow(sum(self.x), 2))
        b = (sum(self.y) - a * sum(self.x)) / self.n
        return Line(a = a, b = b)

    def error(self):
        L = self.bestLine()
        fitted = L.fitPoints(self)
        return sum((self.y - fitted['y']).map(lambda r: math.pow(r, 2)))