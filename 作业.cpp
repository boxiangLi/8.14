//1201
#include <iostream>
using namespace std;
unsigned long long Fibonacci(int n) {
 int m = n - 2;
 if (m > 0) {
  long long first = 1;
  long long second = 1;
  long long temp = 0;
  while (m-- > 0) {
   temp = first;
   first = second;
   second = temp + second;
  }
  return second;
 }
 else {
  cout<<"Please input a number no less than 3";
 }
 cout << endl;
 return 0;
}
int main() {
 int n = 0;
 cin >> n;
 cin.get();
 long long sum = Fibonacci(n);
 cout << sum;
 system("pause");
 return 0;
