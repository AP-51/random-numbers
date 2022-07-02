#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
	
	FILE *fp,*fl;
	float dt[1000000];
	float dt_2[1000000];
	fp=fopen("uni.dat","r");
	fl=fopen("ln.dat","w");
	for(int i=0;i<1000000;i++)
	{
		fscanf(fp,"%f", &dt[i]);
		if(dt[i]<1)
		{
		   dt_2[i]=-2*log(1-dt[i]);
		   fprintf(fl,"%lf\n",dt_2[i]);
		}
	}
	fclose(fp);
	fclose(fl);
	return 0;
}

