"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
    vowels = {'a', 'e', 'i', 'o', 'u'} # set of vowels

    # split phrase along spaces
    words = phrase.split()
    # loop through the phrase
    for i, word in enumerate(words):
        if word[0].lower() in vowels: # account for lower case letters
            new_word = word + "yay"
        else:
            new_word = word[1:] + word[0] + "ay"
        
        words[i] = new_word

    return " ".join(words)
    # at each word, if the first letter is a vowel
    # add yay to end of the word and replace that in the list
    # else if not a vowel
    # create new word with first letter plus yay to the end

    # return the joined list of words


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. REATGAY OBJAY!\n")
