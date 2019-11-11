#ifndef Julia_NDEF
#define Julia_NDEF
#include <complex>
#define MAXITER 256

int iterate(long double x, long double y);
std::complex<long double> julia(std::complex<long double> z, std::complex<long double> c);

#endif