"""
Identified the coordinate with the largest area, ignoring the infites
"""
import sys
import numpy as np

class Coord:
    def __init__(self, line):
        (x, y) = line.split(',')
        self.x = int(x)
        self.y = int(y)

    def distance(self, coord):
        return abs(self.x - coord.x) + abs(self.y - coord.y)

    def distance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def __repr__(self):
        return '%s,%s' % (self.x, self.y)

with open('6/6.input') as f:
    coordinates = []
    max_x = 0
    max_y = 0
    for line in f:
        c = Coord(line)
        if c.x > max_x:
            max_x = c.x
        if c.y > max_y:
            max_y = c.y
        coordinates.append(c)
    print(max_x)
    print(max_y)
    board = [[0 for x in range(max_x)] for y in range(max_y)]
    area = [0 for x in range(len(coordinates))]
    for x in range(max_x):
        for y in range(max_y):
            max_distance = sys.maxsize
            for i in range(len(coordinates)):
                distance = coordinates[i].distance(x, y)
                if distance < max_distance:
                    max_distance = distance
                    board[y][x] = i
                elif distance == max_distance:
                    board[y][x] = '.'
            if board[y][x] != '.':
                area[board[y][x]] += 1
    print(np.matrix(board))

    for x in range(max_x):
        for y in range(max_y):
            if x == 0 or x == max_x-1:
                if board[y][x] != '.':
                    area[board[y][x]] = 0
            if y == 0  or y == max_y-1:
                if board[y][x] != '.':
                    area[board[y][x]] = 0

    print(max(area))