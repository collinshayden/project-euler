# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from math import floor,ceil
import timeit
start = timeit.default_timer()

def primegenerator():
    primeArr = [2]
    x = 3
    while primeArr[-1] < 1000000:
        if isprime(x):
            primeArr.append(x)
        x += 2
    return primeArr

def isprime(n):
    if n == 2:
        return True
    stop = int(ceil(n**0.5)) + 1
    for dividers in range(2,stop, 1):
        if n % dividers == 0:
            return False
    return True

def consecutiveprime():
    primeArr = primegenerator()
    x = 0
    consecutiveArr = []
    for i in range(len(primeArr)):
        x += primeArr[i]
        if x > 1000000:
            break
        if isprime(x):
            consecutiveArr.append(x)
    consecutiveArr.remove(2), consecutiveArr.remove(5)

    return consecutiveArr


print(consecutiveprime())

stop = timeit.default_timer()
print('Time:',stop-start)