from SegmentedPoints import SegmentedPoints
import matplotlib.pyplot as plt


def f(i):
    if i == 1:
        P = SegmentedPoints(30, breakProp = 0.2, sigma = 2, slopeSize = 1)
        plt.figure(1)
        for (i, c) in zip([1, 2, 3], [0, 100, 1000000000]):
            ax = plt.subplot(3, 1, i)
            ax.title.set_text('Cost = {}'.format(c))
            plt.plot(P.df['x'], P.df['y'], **{'color': 'blue', 'marker': 'o'}, label='raw data')
            plt.legend()
            ptpartition = P.segmentedLeastSquares(c)
            print(ptpartition)
            fittedPts = ptpartition.fitPoints()
            plt.plot(fittedPts['x'], fittedPts['y'], **{'color': 'red'}, label='fitted')
            plt.legend()
        plt.show()



if __name__ == '__main__':
    f(1)


