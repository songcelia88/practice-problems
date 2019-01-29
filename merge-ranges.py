"""

    >>> merge_range([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    >>> merge_range([(1, 2), (2, 3)])
    [(1, 3)]

    >>> merge_range([(1, 5), (2, 3)])
    [(1, 5)]

    >>> merge_range([(1, 10), (2, 6), (3, 5), (7, 9)])
    [(1, 10)]

"""

def merge_range(ranges):
    # sort the tuples first

    sorted_ranges = sorted(ranges)
    merged_ranges = [sorted_ranges[0]]
    i=1

    while i < len(sorted_ranges):
        # loop through the rest of the ranges
        # compare the current one with the last one in the merged ranges list
        current = sorted_ranges[i]
        if merged_ranges[-1][1] >= current[0]: # end value is greater than beginning of current
            if merged_ranges[-1][1] <= current[1]: # end value is also less than end value of current
                # replace current entry with the new merged range with end value of the current
                merged_ranges[-1] = (merged_ranges[-1][0],current[1]) 
            # otherwise keep it the same
        else:
            merged_ranges.append(current)
        i=i+1

    return merged_ranges


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT!\n")