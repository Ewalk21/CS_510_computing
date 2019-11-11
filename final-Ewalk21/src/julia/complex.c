#include <stdio.h>
//#include <stdlib.h>
#include <math.h>
#include "complex.h"

COMP add_complex(COMP z, COMP v)
{
    COMP w;
    w.x = z.x + v.x;
    w.y = z.y + v.y;
    return w;
}

COMP square_complex(COMP z)
{
    COMP w;
    w.x = (z.x)*(z.x) - (z.y)*(z.y);
    w.y = 2*(z.x)*(z.y);
    return w;
}

COMP julia(COMP z, COMP c)
{
    return add_complex(square_complex(z),c);
}


long double compAbs(COMP z)
{
    return sqrtl((z.x)*(z.x) + (z.y)*(z.y));
}
