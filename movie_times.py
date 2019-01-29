"""
Write a function that takes an integer flight_length (in minutes) and a list of 
integers movie_lengths (in minutes) and returns a boolean indicating whether 
there are two numbers in movie_lengths whose sum equals flight_length.

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory

Example:
flight_length = 380 min
movie_lengths = [90, 92, 120, 150, 30, 80]

are movie lengths unique?


"""

def movie_times(flight_length, movie_lengths):
    # brute force way:
    # loop through movie times, for each movie time see if you can find the 
    # corresponding movie time that adds to the total flight length (runtime is O(n^2))

    # can you build a dictionary where the key is the movie length and the value
    # is the movie length needed to complete the flight length?

    # e.g. movie_pairs = {90: 380-90, 92: 380-92, ...}
    # loop through this dictionary and see if it's value exists as a key in the dictionary?
    # O(n) runtime? but doesn't account for duplicates

    # alternate is to do counts of movie times
    # movie_pairs = {90: 1, 92: 1, 50: 2, ....}
    # loop through movie lengths
    # if the other length needed is not equal to the current movie length, check dictionary for the existence
    # if the other length needed is equal to the current movie length, check dictionary for existence and that
    # the count is greater than 1
    movie_pairs = {}
    for length in movie_lengths:
        if length not in movie_pairs:
            movie_pairs[length] = 0
        movie_pairs[length] += 1

    for movie in movie_lengths:
        movie2_length = flight_length-movie
        if movie2_length in movie_pairs:
            if movie2_length == movie and movie_pairs[movie]>1:
                return True
            return True

    return False





