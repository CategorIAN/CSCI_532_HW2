from SegmentedPoints import SegmentedPoints
import matplotlib.pyplot as plt


def f(i):
    if i == 1:
        P = SegmentedPoints(30, breakProp = 0.2)
        plt.plot(P.df['x'], P.df['y'], **{'color': 'blue', 'marker': 'o'}, label='raw data')
        plt.legend()
        ptpartition = P.segmentedLeastSquares(10)
        print(ptpartition)
        fittedPts = ptpartition.fitPoints()
        plt.plot(fittedPts['x'], fittedPts['y'], **{'color': 'red'}, label='fitted')
        plt.legend()
        plt.show()



if __name__ == '__main__':
    f(1)


