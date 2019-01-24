"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

If the list is all negative numbers, the subsequence
with the highest sum will be empty (ie, we can do no better
than pick nothing!):

    >>> largest_sum([-1, -2])
    []
"""


def largest_sum(nums):
    """Find subsequence with largest sum."""

    max_sum = 0
    max_sum_idx = 0
    max_length = 0

    sum_sofar = 0
    start_idx = 0
    length = 0

    for i, num in enumerate(nums):
        sum_sofar += num
        length +=1
        if sum_sofar > max_sum:
            max_sum = sum_sofar
            max_sum_idx = start_idx
            max_length = length
        elif sum_sofar <= 0:
            if ((sum_sofar-num) > max_sum):
                max_sum = sum_sofar-num
                max_sum_idx = start_idx
                max_length = length
            sum_sofar = 0
            start_idx = i + 1
            length = 0
        
            
    return nums[max_sum_idx:max_sum_idx+max_length]

if __name__ == '__main__':
    import doctest
    # print(largest_sum([1, 0, 3, -8, 4, -2, 3, -2]))
    # expect [4,-2,3]

    # print(largest_sum([1, 0, 3, -8, 4, -2, 3]))
    # expect [4,-2,3]

    # print(largest_sum([2, -2, 3, -1]))
    # expect [3]

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n")
