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
