#include<stdio.h>
#include"coeffs.h"
#include<math.h>
int main()
{
	FILE *fp,*fq,*fr;
	int x;
	double n,y;
	fp=fopen("gau.dat","r");
	fq=fopen("bern.dat","r");
	fr=fopen("y.dat","w");
	for(int i=0;i<1000000;i++)
	{
		fscanf(fq,"%d",&x);
		fscanf(fp,"%lf",&n);
		y=x*5+n;
		fprintf(fr,"%lf\n",y);
	}
	fclose(fp);
	fclose(fq);
	fclose(fr);
	return 0;
}
