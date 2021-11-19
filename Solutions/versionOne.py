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
        if not bool(re.match(pattern, word)):
            print("Searchable words are only lowercase characters and are less than 24 characters long")
            return False

        # Imports the global row length

        global ROW_LENGTH

        # Generates the rows

        rows = [self.grid[i:i + ROW_LENGTH]
             for i in range(0, len(self.grid), ROW_LENGTH)]

        # Generates the columns

        columns = [list(j) for j in zip(*y)]

        # Searches the rows

        for r in rows:
            if word in "".join(r):
                return True

        # Gearches the columns

        for c in columns:
            if word in "".join(c):
                return True

        return False


# Base code for finding words
if __name__ == '__main__':

    grid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    words_to_find = ["abc"]

    ws = WordSearch(grid, 3)
    print("beginning search")
    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))
