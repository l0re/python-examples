
# import the Python-level symbols of numpy
import numpy as np

# import the C-level symbols of numpy
cimport numpy as np

# numpy must be _always_ initialized when using numpy from C or Cython
np.import_array()

# load cython header
cimport c_test

# wrap function
def fun(np.ndarray indata, np.ndarray outdata):
    assert indata.size == outdata.size
    c_test.fun(<long long*> np.PyArray_DATA(indata),
         indata.size,
         <long long*> np.PyArray_DATA(outdata))

