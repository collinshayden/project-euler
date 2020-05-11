from math import floor, log10
import timeit
start = timeit.default_timer()
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
cache = {}

def factorial_sum(n):
    sum = 0
    for i in range(0, floor(log10(n))+1):
        sum += factorials[n // 10**i % 10]
    return sum

def count_cycles(n):
    cycle = [n]
    loop = False
    while loop != True:
        if cycle[-1] in cache:
            return len(cycle) + cache[cycle[-1]] - 1
        cycle.append(factorial_sum(cycle[-1]))
        if cycle[-1] in cycle[0:-1]: loop = True
    result = len(cycle) - 1
    cache[n] = result
    return result

answer = 0
for i in range(1, 1000000):
    if count_cycles(i) == 60: 
        answer += 1
print(answer)
stop = timeit.default_timer()
print('Time:',stop-start)