
import ctypes as ct
import numpy as np
from numpy.ctypeslib import ndpointer

lib = ct.cdll.LoadLibrary('./libtest.so')
cfun = lib.fun
cfun.restype = None
cfun.argtypes = [ndpointer(ct.c_longlong),
                ct.c_size_t,
                ndpointer(ct.c_longlong)]

def fun(indata, outdata):
    assert indata.size == outdata.size
    cfun(indata, indata.size, outdata)

