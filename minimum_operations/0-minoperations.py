#!/usr/bin/python3
"""
Module: min_operations
----------------------
This module provides a function to calculate the minimum number of operations
needed to achieve exactly `n` H characters in a text file using only two
operations: "Copy All" and "Paste".

"""


def minOperations(n):
    if n < 2:
        return 0

    current_num_of_h = 1
    copied = 0
    num_of_operations = 0

    while current_num_of_h < n:
        if n % current_num_of_h == 0:
            copied = current_num_of_h
            num_of_operations += 1

        current_num_of_h += copied
        num_of_operations += 1
    return num_of_operations
