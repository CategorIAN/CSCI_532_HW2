import pandas as pd
import math
from Line import Line
import numpy as np
from functools import reduce
from PointPartition import PointPartition

class DataPoints:
    def __init__(self, df):
        self.df = df
        self.n = df.shape[0]

    def __str__(self):
        return "Points: [{}: ({}, {}), ... , {}: ({}, {})]".format(self.df.index[0], self.df['x'].iloc[0], self.df['y'].iloc[0],
                                                                  self.df.index[self.n - 1], self.df['x'].iloc[self.n - 1],
                                                                  self.df['y'].iloc[self.n - 1])

    def bestLine(self, i = 0, j = None):
        j = None if j is None else self.n - 1
        (x, y) = (np.array(self.df['x'].iloc[i:j + 1]), np.array(self.df['y'].iloc[i:j + 1]))
        a = (self.n * x @ y - sum(x) * sum(y)) / (self.n * x @ x - sum(x) * sum(x))
        b = (sum(y) - a * sum(x)) / self.n
        return Line(a = a, b = b)

    def leastSquaresError(self, i = 0, j = None):
        j = None if j is None else self.n - 1
        if i >= j:
            return 0
        else:
            L = self.bestLine(i, j)
            fitted = L.fitPoints(self.df['x'].iloc[i:j + 1])
            resids = np.array(self.df['y'].iloc[i:j + 1] - fitted['y'])
            return resids @ resids

    def errorMatrix(self):
        matrix = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(i + 1, self.n):
                matrix[i][j] = self.leastSquaresError(i, j)
        return matrix

    def recoverSegments(self, segmentArray):
        def createBreaks(breaks, end):
            if end < 0:
                return breaks
            else:
                start = segmentArray[end]
                return createBreaks([start] + breaks, start - 1)
        def createSegments(segments, start, breaks):
            if len(breaks) == 0:
                return segments + [DataPoints(self.df.iloc[start:])]
            else:
                nextStart = breaks[0]
                return createSegments(segments + [DataPoints(self.df.iloc[start:nextStart])], nextStart, breaks[1:])
        return createSegments([], 0, createBreaks([], self.n - 1)[1:])


    def segmentedLeastSquares(self, cost):
        def dynamicUpdate(array, j):
            index_errors = [(i, em[i][j] + cost + array[i - 1][1]) for i in range(j + 1)]
            compareTuples = lambda t1, t2: t1 if t1[1] < t2[1] else t2
            (index, error) = reduce(compareTuples, index_errors)
            return array + [(index, error)]

        em = self.errorMatrix()
        tupleArray = reduce(dynamicUpdate, range(1, self.n), [(0, 0)])
        (segmentArray, errorArray) = tuple(zip(*tupleArray))
        print("segmentArray: {}".format(segmentArray))
        return PointPartition(self.recoverSegments(list(segmentArray)), errorArray[self.n - 1])



