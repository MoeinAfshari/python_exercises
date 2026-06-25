# problem 9
'''
pythagorean triplet means a, b, c are natural numbers & a < b < c & a^2 + b^2 = c^2
find product of a, b, c when a, b, c are pythagorean triplet and a+b+c = n
'''

def pythagorean_triplet(n):
    for a in range(1, n+1):
        for b in range(1, n+1-a):
            c = n - (a+b)
            if a**2 + b**2 == c**2 and a < b < c:
                return f"The numbers are {a}, {b}, {c} and the product of them is {a*b*c}"

print(pythagorean_triplet(1000))

