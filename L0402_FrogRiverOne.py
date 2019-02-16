def solution(X, A):
    hops = {}
    try:
        A.index(X)
    except ValueError:
        return -1
    else:
        i = 0
        for a in A:
            hops[a] = 1
            if len(hops) == X:
                return i
            else:
                i += 1

        return -1


def test_example1():
    assert 6 == solution(5, [1, 3, 1, 4, 2, 3, 5, 4])


def test_single_one():
    assert 0 == solution(1, [1])


def test_single_two():
    assert -1 == solution(2, [2])


def test_all_twos():
    assert -1 == solution(2, [2, 2, 2, 2, 2])


def test_large_range():
    assert 29999 == solution(30000, list(range(1, 30001)))


def test_alternating():
    assert 4 == solution(3, [1, 3, 1, 3, 2, 1, 3])
