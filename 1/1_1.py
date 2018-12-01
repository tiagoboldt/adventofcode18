"""
Calculates latest frequency by summing all numbers from input
"""
with open('input.txt') as f:
    print(sum([int(line) for line in f]))
