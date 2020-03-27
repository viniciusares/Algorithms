# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:35:00 2020

@author: VARES
"""

def fat_iter(n_max):
    """Calculates factorial using iteration(for)"""
    output = 1
    for n in range(1, n_max+1):
        print(n)
        output *= n
    return output

def fat_recur(n_max):
    """Calculates factorial using recursion"""
    if n_max == 1:
        return 1
    else:
        return n_max * fat_recur(n_max - 1)

def fibon_iter(n_max):
    """Generates the Fibonacci sequence using iteration"""
    fibon_list = [1, 1]
    if n_max == 1 or n_max == 2:
        return 1
    else:
        for n in range(3, n_max+1):
            fibon_list.append(fibon_list[n - 3] + fibon_list[n - 2])
        return fibon_list

def fibon_recur(n_max):
    """Calculates the Nth Fibonacci number using recursion.
    For inputs between 20 and 30 it's slow.
    For inputs above 30, advance really carefully.
    n=30: 1.2s, n=31: 1.6s, n=32: 2.6s, n=33: 3.2s
    n=34: 4.9s, n=35: 8.1s, n=36: 14.7s
    """
    if n_max > 35:
        raise Exception("Input is too large")
    if n_max == 1 or n_max == 2:
        return 1
    else:
        return fibon_recur(n_max - 1) + fibon_recur(n_max - 2)