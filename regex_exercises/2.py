# problem 2
import re
"""
write a Python program that matches a string that has an a followed by zero or more b's.
"""

def a_followed_by_b(text):
    '''
    text is an input as string
    returns Found a match if it matched completely
    '''
    pattern = re.compile(r"^ab*$")
    text = pattern.search(text)
    return "Not matched!" if text == None else "Found a match!"


# test a_followed_by_b function
print(a_followed_by_b("abc"))
print(a_followed_by_b("abb"))
print(a_followed_by_b("a"))
