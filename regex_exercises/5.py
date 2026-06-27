# problem 5

import re
"""
Found a match if a text has at least three followed b
"""

# text match function
def text_match(text):
    pattern = re.compile(r"b{3,}")
    return "Found a match" if re.search(pattern, text) else "Not match!"


print(text_match("abbb"))
print(text_match("aabbbbc"))
print(text_match("abbddsbser"))

