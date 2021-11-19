import re
# Class for Word Search
class WordSearch(object):
    def __init__(self, grid, ROW_LENGTH):
        self.grid = grid
        self.hashedGrid = {}
        lines = 0

        # Generates the rows
        y = [self.grid[i:i + ROW_LENGTH]
             for i in range(0, len(self.grid), ROW_LENGTH)]

        # Generates the columns
        z = [list(j) for j in zip(*y)]

        # Places every allowed string in each row into the dictionary
        for row in y:
            for i in range(len(row)):
                j = 1
                while j < 24 and i + j <= len(row):
                    self.hashedGrid["".join(row[i:i+j])] = True
                    j += 1

        # Places every allowed string in each column into the dictionary
        for row in z:
            for i in range(len(row)):
                j = 1
                while j < 24 and i + j <= len(row):
                    self.hashedGrid["".join(row[i:i+j])] = True
                    j += 1

    def is_present(self, word):
        # Regular expression matching for allowed strings
        pattern = "([a-z]){1,24}\Z"
        if not bool(re.match(pattern, word)):
            print("Searchable words are only lowercase characters and are less than 24 characters long")
            return False

        # Returns the lookup of the word in the hash table
        return self.hashedGrid.has_key(word)


if __name__ == '__main__':

    # Base code for finding words
    grid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    words_to_find = ["abc"]

    print(words_to_find)
    ws = WordSearch(grid, 3)
    print("beginning search")
    for word in words_to_find:
        if ws.is_present(word):
            print ("found {}".format(word))
