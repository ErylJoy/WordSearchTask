import random
import os.path
import argparse
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')


class RandomWordGen:

    def genNewWords(self, outputFile, num):

        file = open('../Resources/words_alpha.txt', "r")
        words = file.read().splitlines()
        file.close()

        selectedWords = []

        for i in range(num):
            selectedWords.append(words[random.randint(0, len(words)-1)])

        with open(outputFile, "w") as file:
            for line in selectedWords:
                file.write("".join(line) + "\n")

        file.close


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
    parser = argparse.ArgumentParser(
        description='This Program generates a word search with given words')
    parser.add_argument(
        'outputFile', help='The file to output the generated words to')
    parser.add_argument(
        'number', help='The number of words to select')

    args = parser.parse_args()

    number = int(args.number)

    x = RandomWordGen()

    x.genNewWords(args.outputFile, number)
