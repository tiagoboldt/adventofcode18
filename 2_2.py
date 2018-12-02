
"""
Finds common string from two ID pairs
"""
two = 0
three = 0
with open('2.input') as f:
    lines = [line for line in f]
    for i in range(len(lines)):
        reference = lines[i]
        for j in range(i + i, len(lines)):
            comparison = lines[j]
            distance = sum([1 for x, y in zip(reference, comparison) if x.lower() != y.lower()])
            if distance < 2:
                print(distance)
                print(reference)
                print(comparison)