"""
Remove pairs of same letters with difference casing
"""
with open('5/5.input') as f:
    data = list(f.read())
    gap = ord('a') - ord('A')
    i = 0
    while i < len(data)-1:
        if abs(ord(data[i]) - ord(data[i+1])) == gap:
            del data[i:i+2]
            i -= 1
            continue
        i += 1
    print(len(data))
