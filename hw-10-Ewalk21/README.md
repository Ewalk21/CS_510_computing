# CS510 HW 10

**Author(s):** **CHANGEME**

[![Build Status](https://travis-ci.com/chapman-cs510-2017f/hw-10-YOURNAME.svg?token=CHANGEME&branch=master)](https://travis-ci.com/chapman-cs510-2017f/hw-10-YOURNAME)

## Specification

1. Continue reading through the pdf ```Essentials_C_v1.pdf``` to learn more about the ```c``` language. Next week we will continue studying pointers multi-dimensional arrays.

1. Modify your ```fibonacci``` function from HW9 so that it works with the largest unsigned integer type. Put the updated header and source files in ```src/fibonacci/```. Write a function that prints the first 100 Fibonacci numbers, one per line. What is the largest Fibonacci number that you can print before your integer type "overflows" to produce an incorrect answer?
1. In a header ```src/complex/complex.h```, define a structure called ```COMPLEX``` with two fields, ```x``` and ```y```, both of type ```long double```. We will interpret ```x``` as the real part, and ```y``` as the imaginary part.
1. In the source file ```src/complex/complex.c```, define a function ```mult_complex``` that takes two complex structures, ```a``` and ```b```, and returns a complex structure representing their product.  [Recall if ```a = x1 + y1 i``` and ```b = x2 + y2 i```, then ```a * b = (x1 * x2 - y1 * y2) + (x1 * y2 + x2 * y1) i``` ] Think carefully about whether to pass by value or pass by reference in your implementation.
1. In the source file ```src/complex/complex.c``` define a function ```square_complex``` that takes a complex structure and returns the square of that structure.
1. In the source file ```src/complex/complex.c``` define a function ```add_complex``` that takes two complex structures, ```a``` and ```b```, and returns a complex structure representing their sum.  [Recall if ```a = x1 + y1 i``` and ```b = x2 + y2 i```, then ```a + b = (x1 + x2) + (y1 + y2) i``` ]
1. In the source file ```src/complex/complex.c``` define a function ```print_complex``` that takes a complex structure, ```z```, and prints the string "x + y i" where x and y are its real and imaginary parts. Do not print a newline.
1. Ensure the header ```src/complex/complex.h``` contains type definitions for all the above functions properly.
1. In the test file ```test/test_complex.c``` define suitable test functions that demonstrate that ```mult_complex```, ```square_complex```, and ```add_complex``` work as intended.
1. In the source file ```src/complex/print_complex.c``` define a function ```main``` that demonstrates correct printing with ```print_complex```.
1. Edit all your ```Makefile``` files properly so that ```make``` and ```make test``` work as intended. Optionally include ```make clean``` and ```make cleaner``` targets.
1. Discuss your solution in a Jupyter notebook ```Complex.ipynb```. 
1. Push all source and header files to GitHub properly, along with your Jupyter notebook. Make sure Travis runs the tests properly.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
