# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

dividers = [11,12,13,14,15,16,17,18,19,20]
def dividebyall(number):
  for i in range(len(dividers)):
    if(number % dividers[i] != 0):
      return False
  return True

number = 2520
while True:
  if(dividebyall(number)):
    break
  else:
    number += 2520
print(number)
print("done")


