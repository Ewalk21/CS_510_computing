# CS510 HW 9

**Author(s):**  **CHANGEME**

[![Build Status](https://travis-ci.com/chapman-cs510-2017f/hw-09-YOURNAME.svg?token=CHANGEME&branch=master)](https://travis-ci.com/chapman-cs510-2017f/hw-09-YOURNAME)

## Specification

1. Continue reading through the book ```Essentials_C_v1.pdf``` to learn more about the ```C``` language. Next week we will begin studying memory pointers and how C arrays work.
1. Write the header file ```src/fibonacci.h``` for a function ```fibonacci``` that takes an integer ```n``` and returns the ```n```th integer of the Fibonacci sequence (1, 1, 2, 3, 5, ...).
1. Write the corresponding source file ```src/fibonacci.c``` that implements the fibonacci function. Update your Makefiles accordingly.
1. Ensure that the existing tests in ```test/test_fibonacci.c``` run properly. 
1. Write the source file ```src/run_fibonacci.c``` that takes one command line argument ```n```, converts it to an integer with the function ```atoi``` (ascii-to-integer), and prints the value of ```fibonacci(n)``` to the screen. Update your Makefiles accordingly. Verify that everything compiles and that your program runs correctly from the command line. (Hint: you will need the include ```#include <stdlib.h>``` so that C can find the ```atoi``` function in the "standard library" ```stdlib.h```. You will also need to include your own fibonacci header file.)
1. Discuss your solution in a Jupyter notebook ```Fibonacci.ipynb```. Try to think of several cases where your implementation will fail. Test those cases and explain what happens in your notebook. (Hint: use the magic symbol ```%bash``` at the top of a cell to have it run a bash command, or change the running kernel to Bash.) Try to fix those cases, and add tests to demonstrate that they have been fixed. Verify that the tests run correctly.
1. Push all source and header files to GitHub properly, along with your Jupyter notebook. Make sure Travis runs the tests properly and that they pass.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
