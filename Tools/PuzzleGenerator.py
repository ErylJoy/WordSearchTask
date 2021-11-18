import random
import argparse
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')


class PuzzleGenerator():
    def generate(self, outputName, wordName, width, height):

        size = height*width

        file = open(wordName, "r")
        words = file.read().splitlines()
        file.close()
        print(words)

        occupied = []

        attempts = size

        grid = [chr(random.randint(97, 122)) for i in range(0, size)]
        for word in words:
            if random.randint(0, 2) == 0:
                accepted = False
                counter = 0
                while not accepted and counter != attempts:
                    counter += 1
                    row = random.randint(0, height-1)
                    if(width-len(word) == 0):
                        startPos = 0
                    else:
                        startPos = random.randint(0, width-len(word))
                    accepted = True
                    for i in range(len(word)):
                        if i+row*width+startPos in occupied and word[i] != grid[i+row*width+startPos]:
                            accepted = False
                            break
                if counter != attempts:
                    for i in range(len(word)):
                        grid[(row*width)+startPos+i] = word[i]
                        occupied.append(i+row*width+startPos)
                else:
                    print("couldn't insert "+word)

            else:
                accepted = False
                counter = 0
                while not accepted and counter != attempts:
                    counter += 1
                    row = random.randint(0, height)
                    if(width-len(word) == 0):
                        startPos = 0
                    else:
                        startPos = random.randint(0, width-len(word))
                    accepted = True
                    for i in range(len(word)):
                        if width*i+startPos in occupied and word[i] != grid[width*i+startPos]:
                            accepted = False
                            break
                if counter != attempts:
                    for i in range(len(word)):
                        grid[width*i+startPos] = word[i]
                        occupied.append(width*i+startPos)
                else:
                    print("couldn't insert "+word)

        with open(outputName, "w") as file:
            for line in grid:
                file.write(" ".join(line) + "\n")

        file.close


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
    parser = argparse.ArgumentParser(
        description='This Program generates a word search with given words')
    parser.add_argument(
        'outputName', help='The file to output the wordsearch to')
    parser.add_argument(
        'wordName', help='The file to read words to include from')
    parser.add_argument('width', help='Width of the grid')
    parser.add_argument('height', help='Height of the grid')

    args = parser.parse_args()

    height = int(args.height)
    width = int(args.width)

    x = PuzzleGenerator()

    x.generate(args.outputName, args.wordName, height, width)
