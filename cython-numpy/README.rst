
Example
=======

This is a simple demonstration of using cython to call C code from python
to process numpy arrays. 

Usage
=====

The example include both options, either static linkage or dynamic.

1) Static linkage:

.. code:: sh

    $ python setup-static.py build_ext --inplace 

2) Link against a shared C library:

.. code:: sh

    $ gcc -shared -fpic -o libtest.so test/test.c
    $ LDFLAGS="-Ltest" python setup.py build_ext --inplace

3) Now the library can be called in a *native* way like shown in `main.py`_

Explanation
===========

The C function is implemented in `test.c`_. It takes a int64 vector as input
and processes an output vector of the same type.


.. include:: test/test.c
    :code: c

TODO: More explanation.

.. include:: main.py
    :code: py


.. Section links:
.. _ctypes: http://docs.python.org/library/ctypes.html
.. _test.c: test/test.c
.. _test.py: test.py
.. _main.py: main.py
.. _wrapping tool: https://intermediate-and-advanced-software-carpentry.readthedocs.org/en/latest/c++-wrapping.html
