"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True


Let's make sure it works when we can spend over 10 pennies::

    >>> coins(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
    True

"""



def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """
    # if num_coins == 1:
    #     return {1, 10}

    # change = set()
    # prev_coins = coins(num_coins - 1)
    # for coin in prev_coins:
    #     change.add(coin + 10)
    #     change.add(coin + 1)

    # return change

    change = set()
    num_pennies = num_coins
    num_dimes = 0
    penny = 1
    dime = 10

    while num_pennies >=0 and num_dimes <= num_coins:
        change.add(num_pennies*penny + num_dimes*dime)
        num_pennies -= 1
        num_dimes += 1

    return change


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n")
