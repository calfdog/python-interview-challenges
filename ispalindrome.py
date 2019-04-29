"""
 Description: is the string a palindrome
 Developer: Rob Marchetti
"""
def is_palindrome(s):

    def to_chars(s):
        # make lower case
        s = s.lower()
        lowercase_string = ''

        # loop thru each character (char) in string and lower it
        for char in s:
            # test char is alpha char, ignore rest
            if char in "abcdefghijklnopqrstuvwxyz":
                lowercase_string = lowercase_string + char
        return lowercase_string

    def is_pal(s):
        # test to see if string is 0 or 1
        if len(s) <= 1:
            return True
        else:
            # is the first char and last char equal and
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))
