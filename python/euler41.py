from math import sqrt, ceil, floor, log10
import timeit, numpy as np
from unicodedata import digit
start = timeit.default_timer()

def seive(bound):
  boolArr = np.zeros(bound)
  primeArr = []
  boolArr[0] = False; boolArr[1] = False#seive starts at 2, and 0 and 1 are not prime. 

  for i in range(2,bound): 
    boolArr[i] = True#sets all to true

  for a in range(2,ceil(sqrt(bound))+1):
    if boolArr[a]:
      for j in range(a*a, bound, a):
        boolArr[j] = False#sets non primes to false
  
  for p in range(len(boolArr)):
    if boolArr[p] == True:
      primeArr.append(p)

  return primeArr

def digit_length(n):
    return floor(log10(n)) + 1

def is_pandigital(n):
    digits = []
    length = digit_length(n)
    for i in range(length):
        if n % 10 in digits: 
            return False
        digits.append(n % 10)
        n //= 10

    for i in range(1,length+1):
        if i not in set(digits): 
            return False

    return True

def pandigital_primes(bound):
    primes = seive(bound)
    for prime in primes[500000:]:
        if is_pandigital(prime):
            print(prime)


pandigital_primes(100000000)

stop = timeit.default_timer()
print('Time: ',stop-start)