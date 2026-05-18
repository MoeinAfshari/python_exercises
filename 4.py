# problem 4
'''
Find the largest palindrome made from the product of two 3-digits numbers
'''
def palindromic(n): # n is number of digits
    a = 10**(n-1)
    b = 10**n
    ans = max(i * j
        for i in range(a, b)
        for j in range(a, b)
        if str(i * j) == str(i * j)[::-1])
    return ans

# final answer
print(palindromic(3))

   
