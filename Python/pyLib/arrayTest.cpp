#include<iostream>
using namespace std;
int main()
{
  int a[5]={1,5,89,2,2};
  int temp  = a[2];
  temp +=5;
  cout<<temp<<" "<<a[2];
  
  return 0;
}