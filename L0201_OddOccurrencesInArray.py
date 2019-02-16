def solution(A):
    bins = {}
    for a in A:
        if a in bins:
            bins[a] += 1
        else:
            bins[a] = 1

    for b, item in bins.items():
        if item % 2:
            return b


def test_example1():
    assert 7 == solution([9, 3, 9, 3, 9, 7, 9])
