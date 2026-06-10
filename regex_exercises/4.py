# problem 4
import re
"""
Write a Python program that matches a string that has an a followed by zero or one 'b'
"""

def zero_or_one_b(text):
    '''
    text is an input string
    returns Found a match if a followed by zero or one 'b' and otherwise not matched!
    '''
    pattern = "ab?"
    if re.search(pattern, text):
        return "Found a mtch"
    return "Not matched!"

print(zero_or_one_b("abcd"))
