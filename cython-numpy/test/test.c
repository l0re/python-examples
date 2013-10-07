
#include "test.h"

void fun(const long long *indata, size_t size, long long *outdata) 
{
    size_t i;
    for (i = 0; i < size; ++i)
        outdata[i] = indata[i] * 2.0;
}
