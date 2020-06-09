# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?
import numpy as np

def powersum(base, exponent):
  number = base**exponent
  numberStr = str(number)
  digitArray = np.zeros(len(numberStr))

  for i in range(len(numberStr)):
    digitArray[i] = numberStr[i]
 
  digitsum = digitArray.sum()
  print(digitsum)
powersum(2,1000)

#output is 1366
