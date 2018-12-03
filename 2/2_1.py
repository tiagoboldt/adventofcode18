
"""
identifies which set of strings have a letter two or three times and multiples their count
"""
two = 0
three = 0
with open('2/2.input') as f:
    for line in f:
        foundThree = False
        foundTwo = False
        for c in range(ord('a'), ord('z')):
            if not foundThree and line.count(chr(c)) == 3:
                three += 1
                foundThree = True
            elif not foundTwo and line.count(chr(c)) == 2:
                two += 1
                foundTwo = True
    print(three * two)
