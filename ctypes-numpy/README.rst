
Example
=======

This is a simple demonstration of using ctypes to call C code from python
especially to process numpy array type opjects. 

Usage
=====

1) Compile C sources to shared library

.. code:: sh

    $ gcc -shared -fpic -o libtest.so test.c

2) Run the main python file main.py.

.. code:: sh

    $ python main.py

Explanation
===========

The C function is implemented in `test.c`_. It takes a int64 vector as input
and processes an output vector of the same type.


.. include:: test.c
    :code: c

The `test.c`_ file is compiled into a shared libary by 

.. code:: sh

    $ gcc -shared -fpic -o libtest.so test.c

To access the libary we have to load it with ctypes_. For convenient usage
and type checking I recommend to write a small Python wrapper function and 
specify the input interface, like in `test.py`_.

.. include:: test.py
    :code: py

Now the library can be called in a *native* way like shown in `main.py`_:

.. include:: main.py
    :code: py

ctypes_ works on the ABI level and can only be used for C code, not C++. If you
want to interface C++ you either need to write a C wrapper or use a differnt
`wrapping tool`_.

.. Section links:
.. _ctypes: http://docs.python.org/library/ctypes.html
.. _test.c: test.c
.. _test.py: test.py
.. _main.py: main.py
.. _wrapping tool: https://intermediate-and-advanced-software-carpentry.readthedocs.org/en/latest/c++-wrapping.html
