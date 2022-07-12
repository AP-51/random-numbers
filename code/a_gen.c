#include<stdio.h>
#include"coeffs.h"
#include<math.h>
int main()
{
	FILE *f1;
	FILE *f2;
	double v,a;
	f1=fopen("chi.dat","r");
	f2=fopen("agen.dat","w");
	for(int i=0;i<1000000;i++)
	{
		fscanf(f1,"%lf",&v);
                a=sqrt(v);
		fprintf(f2,"%lf\n",a);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
