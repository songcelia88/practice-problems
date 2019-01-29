# modify to do reverse string given a start and end index 

def reverse_string(string):
    """
    Function that takes a list of characters and reverses the letters in place
     stringa = ['c', 'a', 't']
     reverse_string(stringa)
    stringa == ['t', 'a', 'c']

     stringb = ['e', 'v', 'e', 'n']
     reverse_string(stringb)
    stringb == ['n', 'e', 'v', 'e']

    """
    # loop through string from beginning to halfway (if odd round down)
    # take the current letter and the corresponding letter on the end
    # switch the letters in place
    # end_idx = len(str)-1
    # i = 0, str[0] = str[end_idx-i]
    # str[end_idx-i] = str[0]

    end_idx = len(string)-1
    i=0

    while i < len(string)//2:
        current = string[i]
        string[i] = string[end_idx-i]
        string[end_idx-i] = current
        i+=1

    return string

def reverse_words(message):
    """
    Function that takes list of words (as a list of characters and reverses the words) in place


     message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
     reverse_words(message)
    message == [ 's', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ','c', 'a', 'k', 'e']

    """

    # reverse the whole message
    message = reverse_string(message)
    
    i=0
    start_idx = 0
    # then loop through the message find the space or if it's the end
    while i < len(message):
        if message[i] == " ":
            print("found space")
            print("start_idx {}, i {}".format(start_idx, i))
            message[start_idx:i] = reverse_string(message[start_idx:i])
            print(message)
            start_idx = i+1

        elif i == len(message)-1:
            print("end of message")
            print("start_idx ", start_idx)
            message[start_idx:] = reverse_string(message[start_idx:])
            print(message)
        
        i+=1
    # use reverse string to reverse the word from that starting index to the place before the space
    # reset the starting index to be after the space

    

if __name__ == '__main__':
    # import doctest
    # if doctest.testmod().failed == 0:
    #     print("\n*** ALL TESTS PASSED. GREAT!\n")
    message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
    reverse_words(message)
    if message == [ 's', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ','c', 'a', 'k', 'e']:
        print('YAY')



