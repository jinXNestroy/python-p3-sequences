#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    if length == 1:
        print([0])
        return
    fibinacci = [0,1]

    while len(fibinacci) < length:
        next_number = fibinacci[-1] + fibinacci[-2]
        fibinacci.append(next_number)
    print(fibinacci)