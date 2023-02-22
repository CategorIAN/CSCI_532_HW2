from DataPoints import DataPoints
import random
import pandas as pd
from functools import reduce

class SegmentedPoints(DataPoints):
    def __init__(self, size, breakProp = 0, sigma = 1, slopeSize = 1):
        self.sigma = sigma
        self.slopeSize = slopeSize
        xs = list(range(0, size))
        b = self.filter(xs[1:], breakProp)
        print("Intended Breaks: {}".format(b))
        ys = self.generateYs(xs, [], 0, b)
        super().__init__(pd.DataFrame({'x': xs, 'y': ys}))


    def generateYs(self, xs, ys, start, breaks):
        (a, b) = (random.randint(-1 * self.slopeSize, self.slopeSize), 0)
        if len(breaks) == 0:
            return self.getYs(xs, ys, a, b, start)
        else:
            nextStart = breaks[0]
            return self.generateYs(xs, self.getYs(xs, ys, a, b, start, nextStart), nextStart, breaks[1:])

    def getYs(self, xs, ys, a, b, start, end = None):
        if end is None:
            return ys + [a * x + b + random.normalvariate(0, self.sigma) for x in xs[start:]]
        else:
            return ys + [a * x + b + random.normalvariate(0, self.sigma) for x in xs[start:end]]

    def filter(self, xs, prob):
        zs = [[x] if random.random() < prob else [] for x in xs]
        return reduce(lambda l1, l2: l1 + l2, zs)





