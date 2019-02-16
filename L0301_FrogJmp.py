def solution(X, Y, D):
    gap = Y - X

    ret = gap // D
    if gap % D:
        return ret + 1

    return ret


def test_example1():
    assert 3 == solution(10, 85, 30)


def test_X_equals_Y():
    assert 0 == solution(1, 1, 3)


def test_even_gap_and_distance():
    assert 10 == solution(0, 100, 10)


def test_one_big_jump():
    assert 1 == solution(1, 100, 101)
