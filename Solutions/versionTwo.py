import re

ROW_LENGTH = 0
# Class for Word Search
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
        
        # Sets the default of success to false

        success = False
        for i in range(len(self.grid)):
            if self.grid[i] == word[0]:
                if len(word) ==1:
                    return True
                
                # If there is space for the word before the end of the line, try to match horizontally
                if i%ROW_LENGTH+len(word)<=ROW_LENGTH:

                    # Following sets to false if sequence is not present so default is now true
                    success = True
                    
                    # Tests for wach charcter if one is not present, fail
                    for j in range(1, len(word)):
                        if self.grid[i+j] != word[j]:
                            success = False
                            break
                    
                # If the above failed try to match vertically if there is space
                if not success and int((len(self.grid) - i-1)/ROW_LENGTH)>= len(word)-1:
                    # Following sets to false if sequence is not present so default is now true
                    success =True

                    # Tests for wach charcter if one is not present, fail
                    for j in range(1, len(word)):
                        if self.grid[i+ROW_LENGTH*(j)] != word[j]:
                            success = False
                            break

                # If we have been succesful exit the outer loop
                if success: break;
                            

        return success


if __name__ == '__main__':
    # Base code for finding words
    grid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',]

    words_to_find = ['abc']
    print(words_to_find)

    ws = WordSearch(grid,4)
    print("beginning search")
    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))
