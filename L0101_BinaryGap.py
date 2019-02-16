def solution_using_bitmask(N):
    seq_start = False
    counter = 0
    highest = 0
    for i in range(32):
        mask = 1 << i
        if mask > N:
            break

        if mask & N:
            seq_start = True
            if counter > highest:
                highest = counter
            counter = 0
        else:
            if seq_start:
                counter += 1

    return highest


def solution_using_string(N):
    seq_start = False
    counter = 0
    highest = 0
    for b in '{0:b}'.format(N):
        if b == '1':
            seq_start = True
            if counter > highest:
                highest = counter
            counter = 0
        else:
            if seq_start:
                counter += 1
    return highest


def solution(N):
    return solution_using_bitmask(N)


def test_example1():
    assert 2 == solution(9)


def test_example2():
    assert 4 == solution(529)


def test_example3():
    assert 1 == solution(20)


def test_example4():
    assert 0 == solution(15)


def test_example5():
    assert 0 == solution(32)


def test_example6():
    assert 3 == solution(561892)
