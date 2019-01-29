# check to see if a deck of cards is shuffled with a single riffle
# stack of cards is list of integers 1-52 
# loop through the shuffled deck stack
# check first card in shuffled deck
# see if it matches the first card in half1 or half 2
# if it matches either
# pop shuffled deck card, pop the corresponding card in half1 or half2
# if it doesn't then, return False
# if it goes through the whole loop return True

# https://www.interviewcake.com/question/python/single-riffle-check?course=fc1&section=array-and-string-manipulation

def riffle_check(shuffled_deck, half1, half2):
    """ Determine if the shuffled deck is a riffle of half1 and half2
    
        All inputs are lists of numbers 
        Output True if it is a riffle, False if not
    """
    # keep index for shuffled deck, half1 and half2 for better runtime
    half1_idx = 0
    half2_idx = 0
    half1_max_index = len(half1) - 1
    half2_max_index = len(half2) - 1

    for i in range(0,len(shuffled_deck)):
        if half1_idx<=half1_max_index and shuffled_deck[i] == half1[half1_idx]:
            half1_idx +=1
        elif half2_idx<=half2_max_index and shuffled_deck[i] == half2[half2_idx]:
            half2_idx +=1
        else:
            return False

    return True