
from test import fun

import numpy as np

indata = np.ones((5,6), dtype='i8')*4
print indata

outdata = np.zeros((5,6), dtype='i8')
print outdata

fun(indata, outdata)
print outdata

