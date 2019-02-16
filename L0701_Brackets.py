def solution(S):
    o = '([{'
    c = ')]}'

    q = []
    for s in S:
        is_o = o.find(s)
        is_c = c.find(s)
        if is_o >= 0:
            q.insert(len(q), is_o)
        elif is_c >= 0:
            if q:
                prev = q.pop()
                if prev != is_c:
                    return 0
            else:
                return 0

    if q:
        return 0
    else:
        return 1


def test_example1():
    assert 1 == solution('{[()()]}')


def test_example2():
    assert 0 == solution('([)()]')


def test_negative_match():
    assert 0 == solution(')(')


def test_unopened():
    assert 0 == solution('}')
