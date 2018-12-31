"""Given int, print each digit in reverse order, starting with the ones place.

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""
    place = 1
    end_reached = False

    while not end_reached:
        digit = ( (num % (10**place)) - (num % (10**(place-1))) ) / (10**(place-1))
        print(int(digit))

        if num % (10**place) == num:
            end_reached = True

        place += 1

    # shorter solution
    # while num:
    #     next_digit = num % 10
    #     print(next_digit)
    #     num = (num - next_digit) // 10


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
