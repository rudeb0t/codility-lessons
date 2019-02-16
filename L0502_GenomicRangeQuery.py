def pythonic_solution(S, P, Q):
    I = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    # Obvious solution, scalable and compact. But slow for very large S
    # with plenty of entropy.
    result = []
    for a, b in zip(P, Q):
        i = min(S[a:b+1], key=lambda x: I[x])
        result.append(I[i])

    return result


def prefix_sum_solution(S, P, Q):
    I = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    # Faster version using prefix sums as hinted at by the lesson. But has a
    # pretty large space vs time trade-off. It uses both a prefix sum array and
    # a pigeonhole array to keep track fo the impact factor counts.
    n = len(S)
    # Create an array of n+1 pigeon holes to store counts for each impact
    # factor.
    PS = [[0, 0, 0, 0]] * (n + 1)

    # Use prefix sum algorithm to store occurrences of each impact factor in
    # its pigeon hole..
    for k in range(1, n + 1):
        PS[k] = PS[k - 1][:]
        PS[k][I[S[k - 1]] - 1] += 1


    result = []
    for a, b in zip(P, Q):
        # Use prefix sum pigeon holes to count occurences of impact factor for
        # the slice in a, b.
        hits = [i - j for i, j in zip(PS[b+1], PS[a])]

        # This could be generalized into a loop to scan for hit counts. But
        # Since our set is small we can optimize into if..elif..else
        if hits[0]:
            result.append(1)
        elif hits[1]:
            result.append(2)
        elif hits[2]:
            result.append(3)
        else:
            result.append(4)

    return result


def solution(S, P, Q):
    return prefix_sum_solution(S, P, Q)


def test_example():
    assert [2, 4, 1] == solution('CAGCCTA', [2, 5, 0], [4, 5, 6])


def test_single():
    assert [1] == solution('A', [0], [0])


def test_extreme_large_last():
    S = ('T' * 99999) + 'A'
    assert [1] == solution(S, [0], [99999])
