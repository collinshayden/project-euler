# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#these are in euler13.csv
import numpy as np

#importing data
path = "/Users/haydencollins/Desktop/Comp-Sci/data/euler13.csv"
numberArray = np.genfromtxt(path,delimiter=",",dtype=None,encoding='utf-8-sig')

Sum = numberArray.sum()
print(Sum)

#output is 5.5373762303908766e+51
#first 10 digits are 5537376230
