def solution(A):
    uniques = {}
    for a in A:
        uniques[a] = 1

    return len(uniques)


def test_example1():
    assert 3 == solution([2, 1, 1, 2, 3, 1])


def test_extreme():
    i = 100000
    assert i == solution(range(i))


def test_empty():
    assert 0 == solution([])
