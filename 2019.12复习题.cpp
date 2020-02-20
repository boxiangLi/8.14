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
//A5
#include <iostream>
#include <iostream>
using namespace std;
int main()
{
	double b=1 ,a=2,c,i,mun=0 ,n;
	cin>>n;
	for(i=0;i<n;i++)
	{
		mun +=a/b;
		c=a;
		a=a+b;
		b=c;
	}
	printf("%.9f",mun);
}
//A6
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool check(const string &s)
{
	if(s.rfind('A')-s.find('A')==2
	 &&s.rfind('2')-s.find('2')==3
	 &&s.rfind('3')-s.find('3')==4
	 &&s.rfind('4')-s.find('4')==5)
	 return true;
	 return false;
}
int main()
{
	string s="223344AA";
	do
	{
		if(check(s)) cout<<s<<endl;
	}
	while(next_permutation(s.begin(),s.end()));
	return 0;
}
//sing函数
#include<iostream>
using namespace std;
inline int sign(double a)
{
	if(a>0)
	return 1;
	else
	return -1;
}
int main()
{
	double a;
	cin>>a;
	cout<<sign(a);
}
#
