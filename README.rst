
python-examples
===============

Overview
--------

This repository contains sample code for regular tasks when
doing simulation in Python. Python is really great as environment 
for scientific tasks. It allows for rapid prototyping, efficient
programming and together with the additional fast typed array handling
package *numpy* it is also well suited for numerics. 

Moreover, there are many mature additinal packages for scientific computing 
(scipy, sympy, networkx, ...) as well as bindings to allows
major OSS scientific libraries. A native plotting package (*matplotlib*)
complements the functionality and makes it a full fledged replacement for
commercial tools.

The Python interpreter is rather slow compared to plain C/C++ code,
so all computationally intensive tasks should be outsourced to C/C++ routines,
whether by calling existing libraries or integrating own code. Thanks to tools
like Cython, interfacing between Python and C/C++ gets easy and even let 
one choose between different levels of integration.

Examples
--------

* *ctypes-numpy*: Demonstrates how to write a wrapper for an existing shared
  library based on the ABI interface which passes numpy arrays as data.

* *cython-numpy*: Demonstrates interfacing to C library and passing numpy arrays
  with Cython. Cython generates intermediate C wrapper code and could be linked
  either statically or dynamically against the C project.



