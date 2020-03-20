# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?
from math import floor, log10
import timeit
start = timeit.default_timer()

def powerdigit():
    numArr = []
    for base in range(1,10):
        for power in range(1,30):
            num = base**power
            length = floor(log10(num)) + 1
            if length == power:
                print('num:',num,'base:',base,'length:',length)
                numArr.append(num)
    return len(numArr)

print(powerdigit())

stop = timeit.default_timer()
print('Time:',stop-start)

#output is 49