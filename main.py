
ROW_LENTH = 100
import random
# Class for Word Search
class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid

    def is_present(self, word):
        i = 0
        y = [grid[i:i + ROW_LENTH] for i in range(0, len(grid), ROW_LENTH)]
        z = [list(j) for j in zip(*y)]


        word2 = word.split()
        for a in y:
            if word in "".join(a):
                print(1)
                return True

        for a in z:
            if word in "".join(a):
                print(2)
                return True

        return False


# Base code for finding words
grid = ['a','b','c','d','e','f','g','h','i']

file = open("output.txt", "r") 
grid = file.read().splitlines() 
file.close()
print grid


words_to_find = ['cfi']
ws = WordSearch(grid)
print "beginning search"
for word in words_to_find:
    if ws.is_present(word):
        print "found {}".format(word)
