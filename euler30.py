# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
from math import floor, log10
import timeit

start = timeit.default_timer()

def digit(n):
    digitArr = []
    length = floor(log10(n)) + 1#number of digits in n
    for i in range(length):
        digitArr.append(n//10**i % 10)#makes an array of the digits of n
    return digitArr

def digitpower(n):
    digitArr = digit(n)
    digitpowerArr = []
    for num in digitArr: digitpowerArr.append(num**5)
    return digitpowerArr

def digitpowersum(n):
    return(sum(digitpower(n)))

def checker():
    arr = []
    for i in range(999,500000):
        if digitpowersum(i) == i: arr.append(i) 
    return sum(arr)

print(checker())

stop = timeit.default_timer()
print('Time:',stop-start)
#output is 443839, time 2.0152123 seconds