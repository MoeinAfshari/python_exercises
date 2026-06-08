# Problem 1
'''
The sum of all the natural numbers below 1000 that are multiples of 3 or 5
'''
sum_of_nums = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_nums += i
print(sum_of_nums)
