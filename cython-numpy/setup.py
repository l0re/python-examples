from distutils.core import setup, Extension
import numpy
from Cython.Distutils import build_ext

# with dynamic linkage against "libctest.so"
# gcc -shared -fpic -o libtest.so test/test.c
# $LIBRARY_PATH="." python setup.py build_ext --inplace
setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("test",
                 sources=["test.pyx"],
                 libraries=['test'])],
)
