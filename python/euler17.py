# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
from math import floor, log10

units = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8: "eight", 9: "nine"}
teens = {11:"eleven", 12: "twelve", 13: "thirteen", 14:"fourteen", 15:"fifteen", 16: "sixteen", 17:"seventeen", 18: "eighteen", 19: "nineteen"}
tens = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

def digit_length(n):
    if n == 0: return 1;
    return floor(log10(n)) + 1

def number_to_words(n):
    if digit_length(n) == 1: return units[n]
    elif digit_length(n) == 2:
        if n % 10 == 0:
            return tens[n]
        elif n < 20:
            return teens[n]
        else:
            return tens[n - n % 10] + units[n % 10] 
    elif digit_length(n) == 3:
        if n % 100 == 0: return units[n // 100] + "hundred"
        else: return units[n // 100] + "hundred" + "and" + number_to_words(n % 100)
    elif digit_length(n) == 4:
        return units[n // 1000] + "thousand"

letter_count = 0
for i in range(1, 1001):
    print(number_to_words(i))
    letter_count += len(number_to_words(i))

print(letter_count)