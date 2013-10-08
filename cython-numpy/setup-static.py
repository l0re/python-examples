from distutils.core import setup, Extension
import numpy
from Cython.Distutils import build_ext

# static linkage
# $ python setup.py build_ext --inplace
setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("test",
                 sources=["test.pyx", "test/test.c"],
                 include_dirs=[numpy.get_include()])],

