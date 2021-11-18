
import sys
import os.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

import time
import argparse
from Solutions import versionThree as v
from Tools import RandomWordGen
from Tools import PuzzleGenerator
from multiprocessing import Pool
from contextlib import closing

parser = argparse.ArgumentParser(
    description='This Program generates a word search with given words')
parser.add_argument('width', help='Width of the grid')
parser.add_argument('height', help='Height of the grid')
parser.add_argument(
    'numOfWords', help='The file to read words to include from')

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

ws = v.WordSearch(grid, width)

allFound = True
print("beginning search...")
start = time.time()

allFound = True


def dispatch(word):
    if ws.is_present(word):
        print("found {}".format(word))
    else:
        allFound = False


with closing(Pool(processes=5)) as pool:
    pool.map(dispatch, words_to_find)
    pool.terminate()

end = time.time()
print(end - start)
if allFound:
    print("found all")
else:
    print("din't find all")
