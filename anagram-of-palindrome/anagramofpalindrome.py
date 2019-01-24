"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # palindrome - even length: all letter counts are even
    # palinedrom - odd length: all letter counts are event except one letter can have odd count
    # make a dictionary of letter counts
    # if all letter counts are even

    ltr_count = {}

    for char in word:
        if char not in ltr_count:
            ltr_count[char] = 0
        ltr_count[char] += 1

    odd_count = 0
    for letter in ltr_count:
        # if you find an odd letter count
        if (ltr_count[letter] % 2 != 0):
            if (len(word) % 2 == 0): # if the length of the word is even
                return False
            odd_count +=1

    if odd_count > 1:
        return False

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
