#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys



def fib_gen():
    a = 1
    b = 0
    hold = 0
    while True:
        yield a
        hold = a
        a = a + b
        b = hold


def fibonacci(n):
    my_list = []
    g = fib_gen()
    for i in range(n):
        my_list.append(next(g))
    #print(my_list)
    return my_list
