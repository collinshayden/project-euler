from math import sqrt, ceil, floor, log10
import timeit, numpy as np
start = timeit.default_timer()

# finds all primes from 2 to bound, returns a list
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

def truncatable_prime(n, primes):
    # print(1234 // 10)#left to right
    # print(1234 % 1000)#right to left
    if n not in primes:
        return False

    if n in [2,3,5,7]: return False#these are not considered to be truncatable primes

    #left truncatable primes
    for i in range(digit_length(n), 0, -1):
        if n % 10**i not in primes: return False

    #right truncatable primes
    while n // 10 > 0:
        n //= 10
        if n not in primes:
            return False
    return True

def find_truncatable_primes(bound):
    sum = 0
    primes = seive(bound)
    for prime in primes:
        if truncatable_prime(prime, primes):
            print(prime)
            sum += prime
    return sum

print(f"Sum: {find_truncatable_primes(1000000)}")

stop = timeit.default_timer()
print('Time: ',stop-start)