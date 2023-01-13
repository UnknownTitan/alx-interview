#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute -
only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of -
operations needed to result in exactly n H characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    current = 1
    num_of_val_copied = 0
    steps = 0
    while current < n:
        rest = n - current
        if (rest % current == 0):
            num_of_val_copied = current
            current += num_of_val_copied
            steps += 2
        else:
            current += num_of_val_copied
            steps += 1
    return steps
