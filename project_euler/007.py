# problem 7
"""
What is the 10001st prime number?
"""

import math


# checks a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# main function
def find_prime(n):  # n is number of prime numbers
    primes = []
    num = 1
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]


# final answer
if __name__ == "__main__":
    print(find_prime(10001))
