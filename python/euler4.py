# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome():
  products = []
  for i in range(100,1000):
    for j in range(100,1000):
      products.append(i*j)

  for i in range(len(products)):
    temp = products[i]
    temp = str(products[i])

    tempArray = []
    tempReverseArray = []
    palinedomeArray = []
    for j in range(len(temp)):
      tempArray.append(temp[j])
    for k in range(len(temp)-1,-1,-1):
      tempReverseArray.append(temp[k])
    
    if(tempArray == tempReverseArray):
      palinedomeArray.append(tempArray)
      print(palinedomeArray[0])
      
palindrome()
#prints array of all palindromes, largest is 906609
