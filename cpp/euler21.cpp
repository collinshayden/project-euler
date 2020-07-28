// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
// The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
// Evaluate the sum of all the amicable numbers under 10000.
#include <iostream>
using namespace std; 

int factors(int n)
{
  int sum = 0; int step = 1;
  if (n % 2!=0) {//twice as efficient for odd numbers
    step = 2; sum = 1;//sum = 1 because 1 is otherwise skipped for even numbers
  } 
  for (int i = step; i < (n/2) + 1; i+=step){//for normal factors, upper bound is n/2
    if (n % i==0){
      sum += i;
    }
  } return sum;
}

int totalsum()
{
  int totalsum = 0; int perfectnums = 1+6+28+496+8128;
  for (int n = 0; n < 10000; n++){
    if (factors(factors(n)) == n){
      totalsum += n;
      cout<<n<<endl;
    }
  } return totalsum-perfectnums;//question asks for only amicable numbers, excluding perfect numbers(sum of divisers = n)
}

int main()
{
  cout<<totalsum()<<endl;
}

//output is 31626
//time 0m0.359s
