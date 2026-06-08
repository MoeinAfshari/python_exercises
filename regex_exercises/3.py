# problem 3
import re
"""
write a Python program that matches a string that has an a followed by one or more b's.
"""

def a_followed_by_b_v2(text):
    '''
    text is an input as string
    returns not match or found a match
    '''
    text = re.search(r'^ab+$', text)
    return "Not matched!" if text == None else "Found a match!"


# test a_followed_by_b_v2 function
print(a_followed_by_b_v2("a"))
print(a_followed_by_b_v2("ab"))
print(a_followed_by_b_v2("abc"))
