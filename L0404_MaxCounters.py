def solution(N, A):
    ret = [0] * N

    if sum(A)/len(A) == N + 1:
        return ret

    _max = 0
    for a in A:
        if 1 <= a <= N:
            ret[a - 1] += 1
            if ret[a - 1] > _max:
                _max = ret[a - 1]
        elif a == N + 1:
            ret = [_max] * N

    return ret


def test_example1():
    assert [3, 2, 2, 4, 2] == solution(5, [3, 4, 4, 6, 1, 4, 4])


def test_extreme_min():
    assert [1, 0, 0, 0, 0] == solution(5, [1])


def test_extreme_max():
    assert [0, 0, 0, 0, 1] == solution(5, [5])


def test_extreme_max_plus_one():
    assert [0, 0, 0, 0, 0] == solution(5, [6])


def test_single():
    assert [0, 0, 1, 0, 0] == solution(5, [3])


def test_extreme_large():
    assert [0] * 100000 == solution(100000, [100001] * 100000)
