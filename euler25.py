# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:1,1,2,3,5,8,13,21,34,55,89,144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import timeit
start = timeit.default_timer()


def Fibonacci(index):
    if index <= 2:
        raise ValueError('Index too small')
    fibIndex = 2  
    arr = [1,1]
    for i in range(index-2):
        temp = int(arr[0] + arr[1])
        arr[0] = arr[1]
        arr[1] = temp
        fib = temp
        fibIndex += 1
        fibLength = len(str(fib))
    print('Index:',fibIndex,'Length:',fibLength,'Num:',int(fib))

    return fibLength

def digitCount(length):
    i = 3
    while Fibonacci(i) <= length-1:
        i += 1
    print(Fibonacci(i))

digitCount(1000)


stop = timeit.default_timer()
print('Time:',stop-start)