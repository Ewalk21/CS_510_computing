#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sequences
import sys

def main(local_argv):
    try:
        x = int(local_argv[1])
        fib_result = sequences.fibonacci(x)
        print(fib_result[-1])
        return(fib_result[-1])
    except Exception:
        print("invalid input, input must be a positive integer")


if __name__ == "__main__":
    main(sys.argv)


