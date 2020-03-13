# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import numpy as np


def squaresum(lim):
  sum = 0
  for i in range(1,lim):
    sum += i
  square = sum**2
  return(square)
  
def sumofsquares(lim):
  squaresArray = np.zeros(lim)
  for i in range(1,lim):
    squaresArray[i] = i**2
  sumSquares = squaresArray.sum()
  return(sumSquares)

def SumSquareDifference(lim):
  diff = squaresum(lim+1) - sumofsquares(lim+1)
  print(diff)

SumSquareDifference(100)
#output is 25164150
