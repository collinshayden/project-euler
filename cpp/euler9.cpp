// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
// a^2 + b^2 = c^2
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.
#include <iostream>
#include <math.h>

using namespace std;

int triplet()
{
  int powA, powB, powC, abc;
  //having b start at a and c start at b is a significant optimization, making the program ~11 seconds faster
  for (int a = 1; a < 500; a++){
    for (int b = a; b < 500; b++){
      for (int c = b; c < 500; c++){
        if (pow(a,2) + pow(b,2) == pow(c,2)){
          abc = a + b + c;
          if (abc == 1000){
          cout<<"abc = ";cout<<a*b*c<<endl;
          cout<<"a: "; cout<<a; cout<<" b: "; cout<<b; cout<<" c: "; cout<<c<<endl;
          }
        }
      }
    }
  }
}


int main()
{
  triplet();
}

//output is 31875000
//time 2.5s
