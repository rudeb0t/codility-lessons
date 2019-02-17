def solution(S):
    q = []
    for s in S:
        if s == '(':
            q.append(s)
        else:
            try:
                q.pop()
            except IndexError:
                return 0

    if q:
        return 0
    else:
        return 1

def test_example1():
    assert 1 == solution('(()(())())')


def test_example2():
    assert 0 == solution('()))')
