#include<stdio.h>
int main(void)
{
	int s,p,r,q,a,a1,t,n3,n4;
	scanf("%d%d",&s,&p);
	scanf("%d%d",&r,&q);
	a=s*60+p;
	a1=r*60+q;
	if(a>a1)
	{
		t=a-a1;
		n3=t/60;
		n4=t%60;
		printf("%d %d",n1,n2);
	}
	else
	{
		t=a1-a;
		n3=t/60;
		n4=t%60;
		printf("%d %d",n3,n4);
	}
}	
