def solution(A):
    A.sort()
    tail3 = A[-1] * A[-2] * A[-3]
    # Handle first two negative numbers at head of the sorted list.
    head2_tail1 = A[0] * A[1] * A[-1]

    if tail3 > head2_tail1:
        return tail3
    else:
        return head2_tail1


def test_example1():
    assert 60 == solution([-3, 1, 2, -2, 5, 6])


def test_example2():
    assert 125 == solution([-5, 5, -5, 4])
