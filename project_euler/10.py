# problem 10
import math
"""
Find the sum of all the primes below two milions
"""


def sum_primes(limit):
    '''
    sievebound is it because every prime is odd except 2
    sieve[i] == False means the i number is prime
    crosslimit is this because every composite number has at least one factor <= sqrt(limit)
    '''
    sievebound = (limit - 1) // 2
    sieve = [False] * (sievebound + 1)

    crosslimit = (int(math.sqrt(limit)) - 1) // 2

    for i in range(1, crosslimit + 1):
        if not sieve[i]:
            for j in range(2 * i * (i+1), sievebound + 1, 2 * i + 1):
                sieve[j] = True

    # first sum
    sum_primes = 2 # 2 is prime
    for i in range(1, sievebound + 1):
        if not sieve[i]:
            sum_primes += (2 * i + 1) # 2*i + 1 is prime
    return sum_primes


print(sum_primes(2000000))
