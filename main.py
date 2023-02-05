from Polynomial import Polynomial


def f(n):
    X = Polynomial([])
    for i in range(n):
        (P, Q) = (X.randomPoly(i + 1), X.randomPoly(i + 1))
        print("------------------------")
        print("size: {}".format(i+1))
        print("P: {}".format(P))
        print("Q: {}".format(Q))
        print("P * Q the old way: {}".format(P * Q))
        print("P * Q by DFT: {}".format(P.fast_mult(Q, dec=5)))


if __name__ == '__main__':
    f(5)


