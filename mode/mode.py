"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""
    max_freq = 0
    num_dict = {}

    for num in nums:
        if num not in num_dict:
            num_dict[num] = 0
        num_dict[num] += 1
        if num_dict[num] > max_freq:
            max_freq = num_dict[num]

    mode_set = set()
    for key in num_dict:
        if num_dict[key] == max_freq:
            mode_set.add(key)

    return mode_set

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
