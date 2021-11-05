import random


grid = [chr(random.randint(97,124)) for i in range(0, 100000)]

with open("output.txt", "w") as txt_file:
    for line in grid:
        txt_file.write(" ".join(line) + "\n")

txt_file.close