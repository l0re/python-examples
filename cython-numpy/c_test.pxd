
# define the interface used from c header
cdef extern from "test/test.h":
    void fun(const long long *indata, size_t size, long long *outdata) 

