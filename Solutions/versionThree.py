import re
import random

ROW_LENGTH=0   
# Class for Word Search
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

        # For every position in the grid
        for i in range(len(self.grid)):
            if self.grid[i] == word[0]:
                # Verify not running over line or out of grid downwards
                # int() floors
                totalLines = int(len(self.grid)/ROW_LENGTH)
                currentY = int(i/ROW_LENGTH)
                currentX = i%ROW_LENGTH
                # Should we bother checking horizontally from here
                successHoz = currentX + len(word) <= ROW_LENGTH and self.grid[i+len(word)-1] == word[len(word)-1]
                # Should we bother checking vertically from here
                successVert = int((len(self.grid) - i-1)/ROW_LENGTH) >=len(word)-1 and self.grid[i+ROW_LENGTH*(len(word)-1)] == word[len(word)-1]
                # if there is no point looking move on to next starting point
                if not successHoz and not successVert:
                    continue
                #-1 because 
                for j in range(1, len(word)-1):
                    # Python evals lazily so tests space before trying to index out of bounds
                    if successHoz and (self.grid[i+j] != word[j]):
                        successHoz = False
                    if successVert and (self.grid[ROW_LENGTH*j+i] != word[j]):
                        successVert = False
                    if not successHoz and not successVert:
                        break
                if successHoz or successVert:
                    return True
        return False


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

    # Base code for finding words
    # Tests grid
    grid = ['a', 'b', 'c', 'd', ]

    words_to_find = ["gf"]
    print(words_to_find)

    ws = WordSearch(grid, 2)
    print("beginning search")
    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))
