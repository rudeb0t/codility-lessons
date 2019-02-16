def solution(A):
    l = len(A)
    # Build an array of counters for the values that will be contained in A.
    hits = [0] * l

    # Iterate through all the values of A, ignoring zero and negative numbers
    # or any numbers that are not in range of max of A.
    for a in A:
        if a > 0 and a <= l:
            hits[a - 1] += 1

    # Search through the hits and return the first index that does not have a
    # hit.
    for i in range(l):
        if hits[i] == 0:
            return i + 1

    # If we got here, that means we went through all the hits and did not find
    # the smallest positive integer without any hits. So we return the length
    # of A plus one.
    return l + 1


def test_example1():
    assert 5 == solution([1, 3, 6, 4, 1, 2])


def test_example2():
    assert 4 == solution([1, 2, 3])


def test_example3():
    assert 1 == solution([-1, -3])


def test_single_element_negative():
    assert 1 == solution([-1])


def test_single_element_one():
    assert 2 == solution([1])


def test_single_element_two():
    assert 1 == solution([2])


def test_extreme1():
    assert 2 == solution([-1000000, 1])


def test_corner_case1():
    assert 2 == solution([1, 3])
