"""
Identifies the first frequency that appears two times
by repeating the input
"""
seen = {0: True}
freq = 0
found = False
with open('input.txt') as f:
    input = [int(line) for line in f]
    while not found:
        for number in input:
            freq += number
            if freq in seen:
                print(freq)
                found = True
                break
            else:
                seen[freq] = True
