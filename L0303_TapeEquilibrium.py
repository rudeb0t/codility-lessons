# This could have been implemented using prefix sums. But that algorithm does
# not come up until lesson 5. So let's pretend that we don't know about it
# yet...
def solution(A):
    mindiff = 2001
    left = A[0]
    right = sum(A[1:])

    diff = abs(left - right)
    if diff < mindiff:
        mindiff = diff

    if len(A) > 2:
        for i in range(1, len(A) - 1):
            left += A[i]
            right -= A[i]
            diff = abs(left - right)
            if diff < mindiff:
                mindiff = diff

    return mindiff


def test_example():
    assert 1 == solution([3, 1, 2, 4, 3])


def test_double():
    assert 2000 == solution([-1000, 1000])
    assert 2000 == solution([0, 2000])
    assert 0 == solution([2000, 2000])
    assert 1 == solution([1999, 2000])


def test_small():
    assert 20 == solution([-10, -20, -30, -40, 100])
