#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "complex.h"

COMP c;

int main(int argc, char **argv)
{
    if(argc != 9){
        printf("Not the right number of arguments");
        return 0;
    }
    long double xmin = strtold(argv[1],NULL);
    long double xmax = strtold(argv[2],NULL);
    long double ymin = strtold(argv[3],NULL);
    long double ymax = strtold(argv[4],NULL);
    int xpoints = atoi(argv[5]);
    int ypoints = atoi(argv[6]);
    long double creal = strtold(argv[7],NULL);
    long double cimag = strtold(argv[8],NULL);
    c.x = creal;
    c.y = cimag;
    long double dy = (xmax - xmin)/xpoints;
    long double dx = (ymax - ymin)/ypoints;

    int i,j;
    int iter;
    FILE *f;
    f = fopen("juliaSet.csv", "w+");

    for(i = 0; i < xpoints; i++)
    {
        for(j = 0; j < ypoints; j++)
        {
            iter = iterate(xmin + i*dx, ymin + j*dy);
            //output iter  to a csv
            fprintf(f, "%Lf,%Lf,%d\n", xmin + i*dx, ymin + j*dy, iter);
        }
    }
    fclose(f);
    return 0;
}

unsigned int iterate(long double x, long double y)
{
    COMP z;
    z.x = x;
    z.y = y;
    long double mag = sqrtl(z.x*z.x + z.y*z.y);

    if (mag > 2){
        return 1;
    }
    int n = 1;
    while (mag < 2 && n!= MAXITER)
    {
        n ++;
        z = julia(z,c);
        if (mag > 2)
        {
            return n;
        }
    }
    return n;
}




