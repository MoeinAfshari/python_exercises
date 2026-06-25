# problem 3
'''
what is the largest prime factor of the number 600851475143
'''
import math
# this function return all prime factors of n
def prime_factors(n):
    ans = []
    # even factors (2)
    while n % 2 == 0: 
        ans.append(2)
        n = n/2
    # odd factors
    for i in range(3, int(math.sqrt(n)+1), 2):
        while n % i == 0:
            ans.append(i)
            n = n/i
    # last factor if it exists
    if n > 2:
        ans.append(n)
    # prime factors
    return ans

# largest factor
print(max(prime_factors(600851475143)))
