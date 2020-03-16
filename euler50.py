# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
import timeit
start = timeit.default_timer()

def sieve(stop):
    primes = [True for i in range(stop + 1)]
    for i in range(2, stop + 1):
        if primes[i] == True:
            for j in range(i**2, stop + 1, i):
                primes[j] = False
    result = []
    for i in range(len(primes)):
        if primes[i]: result.append(i)
    return result[2:], primes

def solver(lim):
    primes, prime_checker = sieve(lim)
    consecutive_prime_sums = []
    for gap in range(21, 90):
        for i in range(0, len(primes)):
            val = sum(primes[i:i+gap])
            if val > lim: break
            if prime_checker[val]: consecutive_prime_sums.append(val)
    return consecutive_prime_sums[-1]

print(solver(1000000))

stop = timeit.default_timer()
print('Time:',stop-start)
