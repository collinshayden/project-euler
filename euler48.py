# The series, 11 + 22 + 33 + ... + 10**10 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 1000**1000.
import timeit
start = timeit.default_timer()

def selfpowers():
    numArr = []
    total = 0
    for i in range(1,1001):
        numArr.append(i**i)
    for i in numArr:
        total += i
    return total

print(selfpowers())

stop = timeit.default_timer()
print("Time:",stop-start)

#last 10 digits are 9110846700
#time 0.02 seconds