#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

from math import floor, log10
from timeit import default_timer
start = default_timer()

def digit_length(n):
    return floor(log10(n)) + 1

def digit_product(n):
    product = 1
    for i in range(digit_length(n)):
        product *= n % 10
        n //= 10
    return product
    
def adjacent_product(num, adjacent_digits):
    subsequences = []
    largest_product = 0;

    while num > pow(10,adjacent_digits)-1:
        subsequences.append(num % pow(10,adjacent_digits))
        num = num // 10

    for n in subsequences:
        temp_product = digit_product(n)
        if temp_product > largest_product: largest_product = temp_product

    return largest_product


infile = open("euler8_num.txt", "r")
number = int(infile.read())
infile.close()

print(adjacent_product(number,13))

stop = default_timer()
print(f"Time elapsed: {stop-start} seconds")