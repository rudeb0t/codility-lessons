def solution(A, K):
    if len(A) == 0 or K % len(A) == 0:
        return A

    for i in range(K % len(A)):
        a = A.pop()
        A.insert(0, a)

    return A


def test_example1():
    assert [9, 7, 6, 3, 8] == solution([3, 8, 9, 7, 6], 3)


def test_example2():
    assert [0, 0, 0] == solution([0, 0, 0], 1)


def test_example3():
    assert [1, 2, 3, 4] ==  solution([1, 2, 3, 4], 4)


def test_N_equals_A_length():
    assert [3, 8, 9, 7, 6] == solution([3, 8, 9, 7, 6], 5)


def test_N_multiple_of_A_length():
    assert [3, 8, 9, 7, 6] == solution([3, 8, 9, 7, 6], 15)


def test_N_1():
    assert [3, 1, 2] == solution([1, 2, 3], 1)


def test_N_A_length_plus_1():
    assert [3, 1, 2] == solution([1, 2, 3], 4)
    assert [3, 1, 2] == solution([1, 2, 3], 7)


def test_zero_length_A():
    assert [] == solution([], 0)
