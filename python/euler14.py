# // The following iterative sequence is defined for the set of positive integers:
# // n → n/2 (n is even)
# // n → 3n + 1 (n is odd)
# // Using the rule above and starting with 13, we generate the following sequence:
# // 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# // It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# // Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# // Which starting number, under one million, produces the longest chain?
# // NOTE: Once the chain starts the terms are allowed to go above one million.
import timeit
start = timeit.default_timer()

dict = {}#global dictionary

def seq(n):
  count = 1
  while (n > 1):
#if n is in the dictionary, the count value is stored already, saving computation
    if (n in dict):
      count += dict[n]
      return count
#if not, performs the computation
    if n % 2 == 0: n /= 2
    else: n = 3 * n + 1

    count += 1
  return count

def main():
  longestchain = 1
  for i in range(1000000):
    dict[i] = seq(i)
    if (seq(i) > seq(longestchain)):
      longestchain = i
      print(longestchain)

main()

stop = timeit.default_timer()
print('Time: ', stop-start)

#outputs all starting numbers that produce a longer chain than the last
#final output is 837799
#time 2.5 seconds