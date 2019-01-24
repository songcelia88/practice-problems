def findSmallestDifference(A, B, lenA, lenB):
    '''take in one number from list A
    take in one number from list B
    look at the absolute difference
    return the smallest absolute difference

    >>> findSmallestDifference([1, 3], [0], 2, 1)
    1
    
    #Part 2: restructure code to allow for a runtime less than O(n^2)
    #Part 3: discuss the runtime of the restructured code

    '''

    # O(n^2) solution is to loop through each element in A and loop through each element in B for
    # each element in A, find the difference and keep track of the min difference
    # lower runtime: sort the lists?