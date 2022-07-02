#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"coeffs.h"
int main()
{
        printf("Mean:%f\n",mean("gau.dat"));
        printf("Variance:%f\n",variance("gau.dat"));
        return 0;
}

