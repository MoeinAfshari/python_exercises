# problem 6
'''
Find the diffrence between the sum of the squares of the first one hundred natural numbers and the square of the sum
'''
def sum_of_squares(n):
    return sum(map(lambda x: x**2, range(n+1)))

def square_of_sum(n):
    return sum(range(n+1))**2
    
def hence(n):
    return (square_of_sum(n) - sum_of_squares(n))

print(hence(100))
