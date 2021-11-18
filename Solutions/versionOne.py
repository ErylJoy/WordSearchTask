
import random
import re 
# Class for Word Search
ROW_LENGTH =0

class WordSearch(object):
    def __init__(self, grid, rowLen):
        global ROW_LENGTH
        self.grid = grid
        ROW_LENGTH = rowLen

    def is_present(self, word):
        # Regular expression matching for allowed strings
        pattern = "([a-z]){1,24}\Z"
        if bool(re.match(pattern, word)):
            print("Searchable words are only lowercase characters and are less than 24 characters long")
            return False

        # Imports row length
        global ROW_LENGTH
        #generates the rows
        y = [self.grid[i:i + ROW_LENGTH]
             for i in range(0, len(self.grid), ROW_LENGTH)]
        #generats the columns
        z = [list(j) for j in zip(*y)]

        #searches the rows
        for a in y:
            if word in "".join(a):
                return True

        #searches the columns
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
    words_to_find = ["asfaf"]

    ws = WordSearch(grid, 3)
    print("beginning search")
    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))
