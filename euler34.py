# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import timeit
from math import log10, floor
start = timeit.default_timer()


def factorial(n):
    f = 1
    for i in range(n,1,-1):
        f *= i
    return f

def digit(n):
    length = floor(log10(n)) + 1
    digitArr = []
    digitfactorial = []
    factorialsum = 0

    for i in range(length):
        digitArr.append(n//10**i % 10)
        digitfactorial.append(factorial(digitArr[i]))
        factorialsum += digitfactorial[i]
    return factorialsum

def totalsum():
    arr = []
    total = 0
    for i in range(145,99999,1):
        if digit(i) == i:
            arr.append(i)
    for i in range(len(arr)):
        total += arr[i]
    return total


print(totalsum())

stop = timeit.default_timer()
print('Time:',stop-start)
#output is 40730, time 0.5249714 seconds
