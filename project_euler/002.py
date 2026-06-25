# problem 2
'''
Find the sum of all the even-valued fibonacci terms in the sequence which do not exceed four milions
'''
# n is the biggest fibonacci term
def sum_of_fibs(n):
    ans = 0 # sum of even-valued terms
    x = 1 # first term
    y = 2 # second term
    while x <= n:
        if x % 2 == 0:
            ans += x
        x, y = y, x+y
    return ans

# answer of project
print(sum_of_fibs(4000000))
