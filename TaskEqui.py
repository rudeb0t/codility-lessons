def count_total(P, x, y):
    return P[y + 1] - P[x]


def solution(A):
    # Returns the equilibrium indices of the slices that return equal sums.
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]

    equis = []
    for i in range(0, n):
        if count_total(P, 0, i) == count_total(P, i, n - 1):
            equis.append(i)

    try:
        return equis.pop()
    except IndexError:
        return -1


def test_example():
    # 1: sum([-1]), sum([-4, 5, 1, -6, 2, 1])
    # 3: sum([-1, 3, -4]), sum([1, -6, 2, 1])
    # 7: sum([-1, 3, -4, 5, 1, -6, 2])
    assert [1, 3, 7] == solution([-1, 3, -4, 5, 1, -6, 2, 1])
