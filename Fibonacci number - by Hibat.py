#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:33:58 2023

@author: hibatallabenibella
"""

def fib(n):
    a= 0
    b= 1
    print(a)
    print(b)
    for i in range(2,n):
     c=a+b
     a=b
     b=c 
     print(c)
    
fib(5)