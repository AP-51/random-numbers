#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"coeffs.h"
int main()
{
	printf("Mean:%f\n",mean("uni.dat"));
	printf("Variance:%f\n",variance("uni.dat"));
	return 0;
}

