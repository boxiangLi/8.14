//A1
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
//A2
#include <iostream>
using namespace std;
int main()
{
	int a[28],sum=0;
	int j;
	int ave;
	cout<<"输入二十八个整数"<<endl;
	for(int i=0; i<28; i++)
	{
		cin>>a[i];
		sum=sum+a[i];
	 } 
	 ave=sum/28;
	 for(j=0;j<28;j++)
	 {
	 	if(a[j]>ave)
	 	{
		cout<<a[j]<<endl;
	    }
	 }
	 return 0;
}
//A3
#include <iostream>
using namespace std;
int main()
{
	long long int n,m=0,b;
	cout<<"判断是否为回文数：";
	cin>>n;
	b=n;
	while (n>0)
	{
		m=m*10+n%10;
		n/=10;
	 } 
	 if(b==m)
	 cout<<"1"<<endl;
	 else
	 cout<<"0"<<endl;
}
//A4
#include <iostream>
using namespace std;
int main()
{
	int a,b,c,x;
	cin>>a>>b>>c;
	while (c-10>0)
	{
		a=1e10;
		a%=b;
		c=c-10;
	}
	for(int y=0;y<c;y++)
	{
		a*=10;
	}
	x=a/b%10;
	cout<<x;
}
