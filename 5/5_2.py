"""
Remove pairs of same letters with difference casing after removing all
instances of specific letter. Identify which combination generates the
smallest length
"""
with open('5/5.input') as f:
    data = list(f.read())
    gap = ord('a') - ord('A')
    smallest = len(data)
    for ch in range(ord('a'), ord('z')+1):
        data_copy = list(filter(lambda x: x != chr(ch) and x != chr(ch-gap), data))
        print(chr(ch))
        print(chr(ch-gap))
        print(len(data_copy))
        i = 0
        while i < len(data_copy)-1:
            if abs(ord(data_copy[i]) - ord(data_copy[i+1])) == gap:
                del data_copy[i:i+2]
                i -= 1
                continue
            i += 1
        if len(data_copy) < smallest:
            smallest = len(data_copy)
        print(len(data_copy))
    print(smallest)