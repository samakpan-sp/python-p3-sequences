#!/usr/bin/env python3

# def print_fibonacci(length):
#     pass

def print_fibonacci(length):
    fibonacci_sequence = []
    a, b = 0, 1
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    print(fibonacci_sequence)

print_fibonacci(9)
