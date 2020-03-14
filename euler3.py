#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import timeit
from math import floor
start = timeit.default_timer()

def f(x):
    primeArr = []

    for i in range(3,int(floor(x**0.5)),2):
        if (x % i==0):
            if(len(f(i)) == 0):
                primeArr.append(i)

    return primeArr

print(f(600851475143))

stop = timeit.default_timer()
print('Time:', stop - start)
