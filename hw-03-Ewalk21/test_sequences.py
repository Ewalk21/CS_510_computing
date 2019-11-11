#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sequences

def test_1():
     my_list=sequences.fibonacci(1)
     result=my_list[0]
     correct=1
     assert result == correct

def test_2():
      my_list=sequences.fibonacci(2)
      result=my_list[1]
      correct=1
      assert result == correct

def test_3():
      my_list=sequences.fibonacci(10)
      result=my_list[9]
      correct=55
      assert result == correct
