def solution(A):
    # Yep. One line. One try. Python set() is *THAT* awesome!
    return set(range(1, len(A) + 2)).difference(set(A)).pop()


def test_example1():
    assert 4 == solution([2, 3, 1, 5])
