#ifndef Julia_NDEF
#define Julia_NDEF
#define MAXITER 256

struct complex {
    long double x;
    long double y;
};
// Alias the type "COMPLEX" to mean "struct complex"
typedef struct complex COMP;

COMP add_complex(COMP z, COMP w);
COMP square_complex(COMP w);
COMP julia(COMP z, COMP w);
long double compAbs(COMP z);
unsigned int iterate(long double x, long double y);

#endif


