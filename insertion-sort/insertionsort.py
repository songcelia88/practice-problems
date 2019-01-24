"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = list(range(1, 11))

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""
    # need to keep track of the current element you are checking 
    # need to keep track of where you currently are in the array
    # start at the second element
    # compare the second element with the 1st
    # if greater than, move to next element
    # if less than
        # move that element down and check against the next element
        # repeat until you reach the beginning of the array or until you find
        # an element smaller than it

    # what if list is smaller than 2?
    i = 1 # start at the 2nd element

    # loop through the list
    while i < len(alist):
        current = alist[i]

        # if the current number is greater than the previous one, keep it in place
        # move to the next
        if current > alist[i-1]:
            i += 1 
        else:
            j = 1
            while (i-j) >= 0:
                if current > alist[i-j]:
                    break
                alist[i-j+1] = alist[i-j]
                j+=1
            alist[i-j+1] = current
            i+=1

    return alist

def insertion_sort2(alist):
    """Given a list, sort it using insertion sort."""

    # SOLUTION FROM HACKBRIGHT

    for i in range(1, len(alist)):
        # For each item in the list, starting at the second, find out
        # how far to the left it goes--as soon as we find a number
        # smaller than it, we've gone far enough back

        j = i - 1
        while j >= 0 and alist[j] > alist[i]:
            j -= 1
        j += 1

        # now j in the position where we should move i to, and we should
        # put everything over to the right after that

        if j != i:
            alist[j:i + 1] = alist[i:i + 1] + alist[j:i]

    return alist

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE SORTING!\n")
