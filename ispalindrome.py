"""
 Description: is the string a palindrome
 Developer: Rob Marchetti
"""
def is_palindrome(s):

    def to_chars(s):
        # make lower case
        s = s.lower()
        # strip white space
        s = s.replace(" ", "")
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
            # is the first char, last char and middle equal
            return s[0] == s[-1] and is_pal(s[1:-1])
    return is_pal(to_chars(s))


# Examples
# palindrome
s1 = "Was iT a Cat I sAw"
answer1 = is_palindrome(s1)
print("Is '{}' a palindrome?: {}".format(s1, answer1))

# Not a palindrome
s2 = "Is it a Cat I see"
answer2 = is_palindrome(s2)
print("Is '{}' a palindrome?: {}".format(s2, answer2))

# palindrome
s1 = "LeVel"
answer1 = is_palindrome(s1)
print("Is '{}' a palindrome?: {}".format(s1, answer1))

# Not a palindrome
s2 = "Ohio"
answer2 = is_palindrome(s2)
print("Is '{}' a palindrome?: {}".format(s2, answer2))
