# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
import numpy as np
f = 1

def factorial(n):
  global f
  for i in range(n-1,0,-1):
    f *= i

def digitsum(n):
  numberStr = str(n)
  digitArray = np.zeros(len(numberStr))

  for i in range(len(numberStr)):
    digitArray[i] = numberStr[i]
 
  digitsum = digitArray.sum()
  print(digitsum)

factorial(100)
digitsum(f)

#output is 648

