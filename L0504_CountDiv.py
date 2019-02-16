def o1_solution(A, B, K):
    # Algebraic solution, using integer division... No need for prefix sums.
    if A % K:
        return (B // K - ((A // K) + 1)) + 1
    else:
        return (B - A) // K + 1


def obvious_pythonic_solution(A, B, K):
    # Blows up for very large distance between A and B and small K... The
    # prefix sum solution would look similar and so would also blow up for the
    # same A, B, K plus soak up so much RAM for the prefix sum table.
    A += A % K

    count = 0
    for i in range(A, B + 1, K):
        count += 1

    return count


def solution(A, B, K):
    return o1_solution(A, B, K)


def test_example1():
    assert 3 == solution(6, 11, 2)


def test_example2():
    assert 4 == solution(6, 12, 2)


def test_example3():
    assert 2 == solution(6, 11, 3)


def test_example4():
    assert 3 == solution(6, 12, 3)


def test_equal():
    assert 1 == solution(6, 6, 2)


def test_extreme():
    # This is guaranteed to kill any solution that involves a loop, including
    # prefix sums. I don't know why codility put this problem in the prefix sum
    # lesson at all.
    i = 2000000000
    assert i == solution(1, i, 1)
