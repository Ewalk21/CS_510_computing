#!/bin/bash

for i in {1..10}
do
    python fib.py $i >> fibs.csv
done

