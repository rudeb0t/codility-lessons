def count_total(P, x, y):
    return P[y + 1] - P[x]


def solution(A):
    n = len(A)
    P = [0] * (n + 1)
    PA = [0] * (n - 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]

    min_avg = abs(P[k])
    min_avg_idx = 0
    for k in range(n - 1):
        avg_two = count_total(P, k, k + 1) / 2
        if avg_two < min_avg:
            min_avg = avg_two
            min_avg_idx = k

        # Backtrack and do average of three items if we have moved forward
        # enough. Average of three items is enough to predict the minimum
        # average of a slice as far as my tests go. Averaging up to 4 items per
        # slice does not seem to make any difference.
        if k > 0:
            avg_three = count_total(P, k - 1, k + 1) / 3
            if avg_three < min_avg:
                min_avg = avg_three
                min_avg_idx = k - 1

    return min_avg_idx


def test_example():
    assert 1 == solution([4, 2, 2, 5, 1, 5, 8])


def test_double():
    assert 0 == solution([10000, -10000])


def test_simple2():
    assert 2 == solution([-3, -5, -8, -4, -10])
