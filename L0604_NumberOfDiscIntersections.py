def solution(A):
    n = len(A)
    l_point = [0] * n
    r_point = [0] * n
    for i in range(n):
        # Starting point, left of center point
        l_point[i] = i - A[i]
        # Ending point, right of center point
        r_point[i] = i + A[i]

    # sort start end end values.
    l_point.sort()
    r_point.sort()

    intersected = 0
    opened = 0
    i_l = 0
    i_r = 0
    # Scan through our start and end points and count overlapping values.
    for i in range(n):
        while i_l < n:
            if l_point[i_l] > r_point[i_r]:
                # Starting point lies outside ending point. Stop counting.
                break
            # Open another starting point, scan forward.
            opened += 1
            i_l += 1

        # Close up previously opened starting point.
        opened -= 1
        # Accumulate intersected open points.
        intersected += opened
        # Move on to the next ending point.
        i_r += 1
        # Too many intersected counts, return -1 as specified by problem
        # description.
        if intersected > 10000000:
            return -1

    return intersected

def test_example():
    assert 11 == solution([1, 5, 2, 1, 4, 0])


def test_worst_case_zeroes():
    assert 0 == solution([0, 0, 0, 0, 0])


def test_worst_case_ones():
    assert 7 == solution([1, 1, 1, 1, 1])
