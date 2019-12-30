#include <iostream>
using namespace std;
int main()
{
	int a,b,c,d,i=1;
	cin>>a>>b;
	if(a>b)
	{
		c=a,a=b,b=c;
	}
	d=b*i;
	while(d%a != 0)
	{
		i++;
		d=b*i;
	}
	cout<<d<<endl;
	
 } 
