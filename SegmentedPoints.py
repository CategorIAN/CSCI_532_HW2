from DataPoints import DataPoints
import random
import pandas as pd

class SegmentedPoints(DataPoints):
    def __init__(self, size):
        xs = list(range(0, size))
        k = random.randint(0, size - 1)
        b = sorted(random.sample(xs[1:], k))
        ys = self.generateYs(xs, [], 0, b)
        super().__init__(pd.DataFrame({'x': xs, 'y': ys}))

    def generateYs(self, xs, ys, start, breaks):
        (a, b) = (random.choice(range(-9, 10)), random.choice(range(-9, 10)))
        if len(breaks) == 0:
            return self.getYs(xs, ys, a, b, start)
        else:
            nextStart = breaks[0]
            return self.generateYs(xs, self.getYs(xs, ys, a, b, start, nextStart), nextStart, breaks[1:])

    def getYs(self, xs, ys, a, b, start, end = None):
        if end is None:
            return ys + [a * x + b + random.normalvariate(0, 1) for x in xs[start:]]
        else:
            return ys + [a * x + b + random.normalvariate(0, 1) for x in xs[start:end]]



