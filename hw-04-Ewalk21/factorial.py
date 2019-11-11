#!/usr/bin/env python3

###
# Name: Evan A Walker
# Student ID: 01932978
# Email: walke208@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Homework 4
###


import sys


def fac1(n):
    """given n >= 0, fac1(n) will return !n. where !n = n(n-1)(n-2)...(2)
    Args:
        n (int): positive integer parameter. assert n >= 0.
    Returns:
        prod (int): prod = n! = n(n-1)(n-2)...(2)
    """
    assert n >= 0
    if n == 0 or n == 1:
        return 1

    prod = 1
    for i in range(2,n+1):
        prod = prod*i
    return prod

def fac2(n):
    """given n >= 0, fac2(n) will return !n. where !n = n(n-1)(n-2)...(2)
    using a while loop, this function achieves does 2*3*4*...*n which = !n
    Args:
        n (int): positive integer parameter. assert n >= 0.
    Returns:
        prod (int): prod = n! = n(n-1)(n-2)...(2)
    """
    assert n >= 0
    if n == 0 or n == 1:
        return 1

    prod = 1
    count = 1
    while count <= n:
        prod = count*prod
        count += 1
    return prod

def fac3(n):
    """given n >= 0, fac3(n) will return !n. where !n = n(n-1)(n-2)...(2)
    Args:
        n (int): positive integer parameter. assert n >= 0.
    Returns:
        prod (int): prod = n! = n(n-1)(n-2)...(2)
    """
    assert n >= 0
    if n == 0 or n == 1:
        return 1

    prod = 1
    while n >= 2:
        prod = prod * n
        n = n - 1
    return(prod)

def fac4(n):
    """given n >= 0, fac4(n) will return !n. where !n = n(n-1)(n-2)...(2)
    this function achieves this through recursion
    Args:
        n (int): positive integer parameter. assert n >= 0.
    Returns:
        prod (int): prod = n! = n(n-1)(n-2)...(2)
    """
    assert n >= 0
    if n == 0 or n == 1:
        return 1

    if(n == 2):
        return 2
    return n*fac4(n-1)

def fac5(n):
    """given n >= 0, fac5(n) will return !n. where !n = n(n-1)(n-2)...(2)
    this function achieves it using a generator and a for loop
    Args:
        n (int): positive integer parameter. assert n >= 0.
    Returns:
        prod (int): prod = n! = n(n-1)(n-2)...(2)
    """
    assert n >= 0
    if n == 0 or n == 1:
        return 1

    def fac5gen():
        n = 0
        while True:
            n += 1
            yield n
    g = fac5gen()
    prod = 1
    for i in range(n):
        prod = next(g)*prod
    return prod



#print(fac1(0))
#print(fac2(1))
#print(fac3(1))
#print(fac4(1))
#print(fac5(1))