"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    prime_list = []
    # generate numbers starting from 2 and check if prime
    # if prime, add to the list
    # continue until length of the list is equal to count
    # while 

    # check if number is prime
    # check for the simple cases: 0, 1, 2 and return for those
    # check if divisible by 2, if so return False
    # then check for all odd divisors up until n/2 (or sqrt(n))
    # if any of those return mod = 0, then return False
    # otherwise return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
