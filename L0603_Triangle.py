def solution(A):
    A.sort()
    for i in range(len(A) - 2):
        if all((A[i] + A[i+1] > A[i+2],
               A[i+1] + A[i+2] > A[i],
               A[i+2] + A[i] > A[i+1])):
            return 1
    return 0


def test_example1():
    assert 1 == solution([10, 2, 5, 1, 8, 20])


def test_example2():
    assert 0 == solution([10, 50, 5, 1])
