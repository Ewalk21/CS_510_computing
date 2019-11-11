#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <complex>
#include "mandelbrot.h"
#define MAXITER 256

std::complex<long double> z;

int main(int argc, char **argv)
{
    if(argc != 9){
        printf("Not the right number of arguments \n");
        return 0;
    }
    long double xmin = strtold(argv[1],NULL);
    long double xmax = strtold(argv[2],NULL);
    long double ymin = strtold(argv[3],NULL);
    long double ymax = strtold(argv[4],NULL);
    int xpoints = atoi(argv[5]);
    int ypoints = atoi(argv[6]);
    long double zreal = strtold(argv[7],NULL);
    long double zimag = strtold(argv[8],NULL);
    std::complex<long double> ztemp (zreal,zimag);
    z = ztemp;
    long double dy = (xmax - xmin)/xpoints;
    long double dx = (ymax - ymin)/ypoints;

    int i,j;
    int iter;
    std::ofstream myfile;
    myfile.open ("juliaSet.csv");
    for(i = 0; i < xpoints; i++)
    {
        for(j = 0; j < ypoints; j++)
        {
            iter = iterate(xmin + i*dx, ymin + j*dy);
            //output iter  to a csv
            myfile << xmin + i*dx << "," << ymin + j*dy << "," << iter << std::endl;
        }
    }
    myfile.close();
    return 0;
}

int iterate(long double x, long double y)
{
    std::complex<long double> c (x,y);
    long double ab = std::abs(c);
    if (ab > 2){
        return 1;
    }
    int n = 1;
    while (ab < 2 && n!= MAXITER)
    {
        n ++;
        c = julia(z,c);
        ab = std::abs(c);
        if (ab > 2)
        {
            return n;
        }
    }
    return n;
}

std::complex<long double> julia(std::complex<long double> z, std::complex<long double> c)
{
    return z*z + c;
}










