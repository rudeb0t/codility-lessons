def solution(A):
    L = len(A)
    hits = [0] * L

    for a in A:
        if 0 < a <= L:
            if hits[a - 1] > 0:
                return 0
            else:
                hits[a - 1] += 1
        else:
            return 0

    return 1


def solution_using_dict(A):
    hits = {}
    hitsum = 0
    _max = 1
    for a in A:
        if a > _max:
            _max = a

        hitsum += a
        if a in hits:
            return 0
        else:
            hits[a] = 1

    if hitsum != _max * (_max + 1) / 2:
        return 0

    return 1


def test_example1():
    assert 1 == solution([4, 1, 3, 2])


def test_example2():
    assert 0 == solution([4, 1, 3])


def test_extreme_min_max():
    assert 1 == solution([1])
    assert 0 == solution([2])

def test_double():
    assert 0 == solution([1, 1])
    assert 0 == solution([2, 3])
