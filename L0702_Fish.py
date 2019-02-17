def solution(A, B):
    alives = []
    alive_count = 0
    for aq, bq in zip(A, B):
        if bq == 0:
            while len(alives):
                if alives[-1] > aq:
                    break
                else:
                    alives.pop()
            else:
                alive_count += 1
        else:
            alives.append(aq)

    return alive_count + len(alives)


def test_example1():
    # Fish 0 and 4 remain.
    assert 2 == solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])


def test_example2():
    # Fish 4 remain.
    assert 1 == solution([4, 3, 2, 1, 5], [1, 1, 1, 1, 0])


def test_example3():
    # Fish all swim upstream and never meet.
    assert 5 == solution([4, 3, 2, 1, 5], [0, 0, 0, 0, 0])


def test_example4():
    # Fish 4 remain.
    assert 1 == solution([4, 3, 2, 1, 5], [1, 0, 0, 0, 0])


def test_example5():
    # Fish swimming upstream never meet with the largest fish at the end of the
    # stream.
    assert 5 == solution([4, 3, 2, 1, 5], [0, 0, 0, 0, 1])
