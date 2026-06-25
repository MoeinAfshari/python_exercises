# problem 5
'''
What is the smallest number that is evenly divisible by all of the numbers from 1 to 20
'''
import math
def lcm(n): # n is last number
    return math.lcm(*range(1, n+1))

# final answer
print(lcm(20))
