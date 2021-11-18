
import random
# Class for Word Search


class WordSearch(object):
    def __init__(self, grid, ROW_LENGTH):
        self.grid = grid
        self.hashedGrid = {}
        lines = 0

        y = [self.grid[i:i + ROW_LENGTH]
             for i in range(0, len(self.grid), ROW_LENGTH)]
        z = [list(j) for j in zip(*y)]
        for row in y:
            for i in range(len(row)):
                j = 1
                while j < 24 and i + j <= len(row):
                    self.hashedGrid["".join(row[i:i+j])] = True
                    j += 1
        for row in z:
            for i in range(len(row)):
                j = 1
                while j < 24 and i + j <= len(row):
                    self.hashedGrid["".join(row[i:i+j])] = True
                    j += 1

    def is_present(self, word):
        return self.hashedGrid.has_key(word)


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

    # Base code for finding words
    grid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    words_to_find = ["ad"]

    print words_to_find
    ROW_LENGTH = 3
    ws = WordSearch(grid)
    print "beginning search"
    for word in words_to_find:
        if ws.is_present(word):
            print "found {}".format(word)
