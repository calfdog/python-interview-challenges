"""
    Description: Problem: Given two strings, check whether two given strings are an anagram of each other or not.
    An anagram of a string is another string that contains same characters, only the order of characters can be
    different.

    For example, "Listen" and "Silent" are an anagram of each other.
    Developer: Rob Marchetti
"""

# Returns True - these are anagrams
string1 = "Listen"
string2 = "Silent"
string3 = "Conversation"
string4 = "Voices rant on"

# Returns False these are not anagrams
string5 = "Conversation"
string6 = "Voices Bant on"
string7 = "Listen"
string8 = "Silently"


def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # create a hash map
    hmap = dict()

    if len(str1) != len(str2):
        return False

    """
    loop through string 1 is the char exists increment by one, else if this is the 
    first time the char is seen set it to one
    """
    for c in str1:
        if c in hmap:
            hmap[c] += 1
        else:
            hmap[c] = 1

    # loop through string 2 is the char exists decrement by one, else if this is the
    # first time the char is seen set it to one
    for c in str2:
        if c in hmap:
            hmap[c] -= 1
        else:
            hmap[c] = 1

    # loop thru each char i any is set to zero return False otherwise return True
    for c in hmap:
        if hmap[c] != 0:
            return False
    return True



results = is_anagram(string1, string2)
print(results)
