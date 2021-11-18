
import random
# Class for Word Search
ROW_LENGTH =0

class WordSearch(object):
    def __init__(self, grid, rowLen):
        global ROW_LENGTH
        self.grid = grid
        ROW_LENGTH = rowLen

    def is_present(self, word):
        global ROW_LENGTH
        y = [self.grid[i:i + ROW_LENGTH]
             for i in range(0, len(self.grid), ROW_LENGTH)]
        z = [list(j) for j in zip(*y)]
        for a in y:
            if word in "".join(a):
                return True

        for a in z:
            if word in "".join(a):
                return True

        return False


# Base code for finding words
if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

    grid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    words_to_find = ["a"]

    ws = WordSearch(grid)
    print "beginning search"
    for word in words_to_find:
        if ws.is_present(word, 3):
            print "found {}".format(word)
