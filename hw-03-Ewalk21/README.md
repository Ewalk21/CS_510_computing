# CS510 HW 3

**Author(s):** **CHANGEME**

[![Build Status](https://travis-ci.com/chapman-cs510-2017f/hw-03-YOURNAME.svg?token=CHANGEME&branch=master)](https://travis-ci.com/chapman-cs510-2017f/hw-03-YOURNAME)

## Specification

1. Continue reading and working through the following resources on Python to review how Python works, what its syntax is, and how basic control and data structures work. 
    * [Python Interactive Tutorial](http://learnpython.org/)
    * [Getting Started with the Python Language](http://www.scipy-lectures.org/intro/language/python_language.html)
1. Complete the classwork, in collaboration with your group (using Slack as needed). 
1. After finishing the classwork, let us _refactor_ number 1 of CW03. Copy your code files into this repository and commit them. Then rewrite the function ```fibonacci(n)``` so that it uses a _generator_ created by a new function ```fib_gen()```. The rest of the code that you wrote for CW03 should remain unchanged. Verify that all your test cases still work properly after refactoring.
    * Hint: ```f = fib_gen()``` should produce a generator, such that ```next(f)``` returns the next fibonacci integer. Do not put an end-condition on this generator, so that in principle it can generate the entire infinite sequence of fibonacci numbers.
    * Hint: ```fibonacci(n)``` should create a list that contains the first ```n``` outputs yielded by ```fib_gen()```.
    * Hint: As an example, the following code produces a generator for the set of positive integers. The keyword ```yield``` simply replaces ```return```: it returns a value while preserving the running state of the generator. The next time the generator is called, it resumes where it left off until it reaches the next ```yield``` or ```return``` statement. It may also be concise to use a _list comprehension_ for the refactoring, as shown below, where a list of 5 elements taken from the integer generator is created.
```python
def gen_ints():
    """Generator for the positive integers."""
    n = 1
    while True:
        yield n
        n += 1

g = gen_ints()
[next(g) for _ in range(5)]
```

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
