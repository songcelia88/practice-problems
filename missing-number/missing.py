"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """

    # O(n) implementation (easiest)
    # num_set = set(nums)

    # for i in range(1, max_num+1):
    #     if i not in num_set:
    #         return i

    # O(nlogn) implementation
    # nums.sort()

    # for i in range(1, max_num+1):
    #     if i != nums[i-1]:
    #         return i

    # O(n) runtime O(1) run space
    ideal_sum = 0
    for i in range(1,max_num+1):
        ideal_sum += i

    actual_sum = 0
    for num in nums:
        actual_sum += num

    return ideal_sum - actual_sum

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
