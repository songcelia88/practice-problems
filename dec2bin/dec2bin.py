"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

And finally, using division:

    >>> dec2bin_division(0)
    '0'

    >>> dec2bin_division(1)
    '1'

    >>> dec2bin_division(2)
    '10'

    >>> dec2bin_division(4)
    '100'

    >>> dec2bin_division(15)
    '1111'

my solution
    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'

"""


def dec2bin(num):
    """Convert a decimal number to binary representation."""
    bin_num = [str(num%2)]
    current = num // 2

    while current > 0:
        bin_num.insert(0, str(current%2))
        current = current // 2

    return "".join(bin_num)


def dec2bin_backwards(num):
    """Convert a decimal number to binary representation."""

    # Work backwards, finding the least-significant-bit first,
    # moving up to the most-significant bit.
    #
    # At the end, print the list of bits reversed

    result = []
    place = 0

    while place == 0 or num >= 2 ** place:

        if num % (2 ** (place + 1)):
            num -= 2 ** place
            result.append("1")

        else:
            result.append("0")
        place += 1

    return "".join(reversed(result))

    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
