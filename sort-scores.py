def sort_scores(unsorted_scores, highest_possible_score):
    """
    return a list of the scores sorted from highest to lowest in O(n) time
    """

    # make a dictionary of scores and their counts 
    # countdown from the highest score and see if it exists in the dictionary
    # if it does, append that to the list x number of times depending on the count
    # return that list
    score_dict = {}
    min_score = unsorted_scores[0]
    max_score = unsorted_scores[0]
    sorted_scores = []
    
    for score in unsorted_scores:
        if score not in score_dict:
            score_dict[score] = 0
        score_dict[score] +=1

        if score > max_score:
            max_score = score

        if score < min_score:
            min_score = score

    # 