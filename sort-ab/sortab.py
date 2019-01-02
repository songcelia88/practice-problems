"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    lst = []

    # while (len(a) != 0) or (len(b) != 0):
    #     if len(a) == 0:
    #         lst.append(b.pop(0))
    #     elif len(b) == 0:
    #         lst.append(a.pop(0))
    #     else:
    #         if a[0] <= b[0]:
    #             lst.append(a.pop(0))
    #         else:
    #             lst.append(b.pop(0))

    # alternate solution that doesn't use pop(0)
    idx_a = 0
    idx_b = 0

    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] < b[idx_b]:
            lst.append(a[idx_a])
            idx_a += 1
        else:
            lst.append(b[idx_b])
            idx_b += 1

    lst.extend(a[idx_a:])
    lst.extend(b[idx_b:])

    return lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
