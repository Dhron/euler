#include <stdio.h>

int main()
{
int f0 = 1;
int f1 = 1;
int fn = 0;
int sumEven = 0;
while(fn <= 4000000)
{
//doing my incrementations of the recursive formula
	fn = (f0 + f1);
	f0 = f1;
	f1 = fn;
	//printf("%d\n", fn);
	if(fn%2 == 0)
	{
		sumEven += fn;
	}
}
printf("%d\n", sumEven);
return sumEven;
}
