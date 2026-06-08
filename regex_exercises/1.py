# problem 1
import re
"""
write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
"""

def allowed_characters_check(text):
    '''
    text is an input as string 
    returns True if mached & False if not matched
    '''
    pattern = re.compile(r"[^a-zA-Z0-9]+")
    text = re.search(pattern, text)
    return not bool(text)


# test allowed_characters_check function
print(allowed_characters_check("sggdssgi#{w}AF34dfs"))
print(allowed_characters_check("heloo34sdf"))
