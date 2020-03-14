# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import timeit
from math import ceil
start = timeit.default_timer()

def isprime(x):
  stop = int(ceil(x ** 0.5))
  for dividers in range(3,stop + 1,2):
    print(dividers)
    if x % dividers == 0:
      return False
  return True


def primes(max=10):
  yield 2
  found = 1
  current = 3
  while found < max:
    if isprime(current):
      yield current
      found += 1
    current += 2


for prime in primes(10001):
  print(prime)

stop = timeit.default_timer()

print('Time:',stop-start)
#output is 104743
