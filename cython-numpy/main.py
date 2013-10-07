
from test import fun

import numpy as np

indata = np.ones((5,6), dtype='i8')
print indata

outdata = np.zeros((5,6), dtype='i8')
print outdata

fun(indata, outdata)
print outdata

indata *= 2
fun(np.array(indata), outdata)
print outdata

