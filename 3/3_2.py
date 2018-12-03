"""
Identifies portion of fabric used by single claim
"""

import re

SIZE = 1000
fabric = [[0 for x in range(SIZE)] for y in range(SIZE)]
reused_area = 0

class Config():
    def __init__(self, line):
        regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        match = regex.search(line)
        self.ID = int(match.group(1))
        self.left = int(match.group(2))
        self.top = int(match.group(3))
        self.width = int(match.group(4))
        self.height = int(match.group(5))


with open('3/3.input') as f:
    for line in f:
        config = Config(line)
        for i in range(config.top, config.top+config.height):
            for j in range(config.left, config.left+config.width):
                fabric[i][j] = config.ID
    f.seek(0)
    for line in f:
        config = Config(line)
        full = True
        for i in range(config.top, config.top+config.height):
            for j in range(config.left, config.left+config.width):
                if fabric[i][j] is not config.ID:
                    full = False
                fabric[i][j] = config.ID
        if full:
            print(config.ID)
