if True:
    import sys
    import os.path
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

import time
from Tools import PuzzleGenerator
from Tools import RandomWordGen


def test(ws, theGrid, theWidth):
    ws = v.WordSearch(theGrid)

    allFound = True
    print "beginning search..."
    start = time.time()
    for word in words_to_find:
        if ws.is_present(word, theWidth):
            print "found {}".format(word)
        else:
            allFound = False

    end = time.time()
    timeTaken = end-start
    print(end - start)
    if allFound:
        print "found all"
    else:
        print "din't find all"
    return timeTaken


parser = argparse.ArgumentParser(
    description='This Program generates a word search with given words')
parser.add_argument('width', help='Width of the grid')
parser.add_argument('height', help='Height of the grid')
parser.add_argument(
    'numOfWords', help='The file to read words to include from')

args = parser.parse_args()

width = args.width
height = args.height
numOfWords = args.numOfWords

wg = RandomWordGen()
wg.genNewWords("Resources/tempwords.txt", numOfWords)

pg = PuzzleGenerator()
pg.generate('Resources/temppuzzle.txt',
            'Resources/tempwords.txt', width, height)


print "loading puzzle..."
file = open("Resources/temppuzzle.txt", "r")
grid = file.read().splitlines()
file.close()


print "loading words to find..."
file = open("Resources/testwords.txt", "r")
words_to_find = file.read().splitlines()
file.close()
if True:
    from Solutions import versionOne as v
v1T = test(v, grid, width)

if True:
    from Solutions import versionTwo as v
v2T = test(v, grid, width)

if True:
    from Solutions import versionThree as v
v3T = test(v, grid, width)

if True:
    from Solutions import versionFour as v

start = time.time()
print "Building searcher..."
ws = v.WordSearch(grid, width)

allFound = True
print "beginning search..."

for word in words_to_find:
    if ws.is_present(word):
        print "found {}".format(word)
    else:
        allFound = False

end = time.time()
v4T = end-start
print(end - start)
if allFound:
    print "found all"
else:
    print "din't find all"

print "end"


print "Version One Time: "+str(v1T)+"\nVersion Two Time: "+str(v2T) + \
    "\nVersion Three Time: "+str(v3T)+"\nVersion Four Time: "+str(v4T)


os.remove("Resources/temppuzzle.txt")
os.remove("Resources/tempwords.txt")
