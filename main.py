from Polynomial import Polynomial


def f(i):
    if i == 1:
        P = Polynomial([1, 4, 8])
        print(P.coeffs[-1])
        print(P.coeffs[P.deg-1:-1:-1])
        print(P(2))
    if i == 2:
        P = Polynomial([2, 4, 3, 9, 7])
        print(P.even())
        print(P.odd())
    if i == 3:
        P = Polynomial([2, 4, 3, 9, 7])
        print(P.padded())
    if i == 4:
        P = Polynomial([1, 3, 1, 1])
        print(P.DFT())
    if i == 5:
        P = Polynomial([1, 2, 1])
        Q = Polynomial([-1, 0, 1])
        print(P.fast_mult(Q, dec = 4))
    if i == 6:
        P = Polynomial([1, 1, 2])
        Q = Polynomial([-1, 1])
        print(P * Q)


if __name__ == '__main__':
    f(6)


