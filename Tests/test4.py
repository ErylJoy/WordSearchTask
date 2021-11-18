import sys
import os.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')


from Tools import PuzzleGenerator
from Tools import RandomWordGen
from Solutions import versionFour as v
import time
import argparse


parser = argparse.ArgumentParser(description='This Program generates a word search with given words')
parser.add_argument('width', help='Width of the grid')
parser.add_argument('height', help='Height of the grid')
parser.add_argument('numOfWords', help='The file to read words to include from')

args = parser.parse_args()

width = int(args.width)
height = int(args.height)
numOfWords = int(args.numOfWords)

wg = RandomWordGen.RandomWordGen()
wg.genNewWords("../Resources/tempwords.txt", numOfWords)

pg = PuzzleGenerator.PuzzleGenerator()
pg.generate('../Resources/temppuzzle.txt',
            '../Resources/tempwords.txt', width, height)


print("loading puzzle...")
file = open("../Resources/temppuzzle.txt", "r")
grid = file.read().splitlines()
file.close()


print("loading words to find...")
file = open("../Resources/tempwords.txt", "r")
words_to_find = file.read().splitlines()
file.close()

print("loading solver...")
start = time.time()
ws = v.WordSearch(grid, width)
end = time.time()
print("build time: "+str(end - start))

allFound = True
print("beginning search...")
start = time.time()
ROW_LENGTH = width
for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))
    else:
        allFound = False


end = time.time()
print(end - start)
if allFound:
    print("found all")
else:
    print("din't find all")

os.remove("../Resources/temppuzzle.txt")
os.remove("../Resources/tempwords.txt")
