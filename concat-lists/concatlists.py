"""Given two lists, concatenate the second list at the end of the first.

For example, given ``[1, 2]`` and ``[3, 4]``::

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]

It should work if either list is empty::

    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
"""


def concat_lists(list1, list2):
    """Combine lists."""
    result = []

    for item in list1:
        result.append(item)

    for item in list2:
        result.append(item)

    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
