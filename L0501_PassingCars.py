def solution(A):
    count = 0
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]

    for i in range(n - 1):
        if A[i] == 0:
            count += P[n] - P[i]

    if count > 1000000000:
        return -1
    else:
        return count


def test_example():
    assert 5 == solution([0, 1, 0, 1, 1])


def test_last_pair():
    assert 1 == solution([0, 1])
    assert 2 == solution([0, 0, 1])


def test_single():
    assert 0 == solution([0])
    assert 0 == solution([1])


def test_all_zero():
    assert 0 == solution([0, 0, 0])


def test_all_one():
    assert 0 == solution([1, 1, 1])


def test_extreme_all_zero():
    assert 0 == solution([0] * 100000)


def test_extreme_all_one():
    assert 0 == solution([1] * 100000)


def test_alternate():
    assert 10 == solution([1, 0] * 5)
    assert 15 == solution([0, 1] * 5)
