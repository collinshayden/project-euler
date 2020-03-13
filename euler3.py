#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def f(x):
    factors = []
    tempArr = []
    nonprime = []
    primefactors = []

    for i in range(2,x):
        if (x % i==0):
            factors.append(i)

    for index in range(len(factors)):
        for divider in range(2,factors[index]):
            if(factors[index] % divider == 0):
                tempArr.append(factors[index])
                nonprime = list(set(tempArr))

    for i in range(len(nonprime)):
        factors.remove(nonprime[i])

    largestPrimeFactor = factors[len(factors)-1]
    return largestPrimeFactor

print(f(600851475143))
