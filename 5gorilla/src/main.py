import sys
import math
from datetime import datetime

def main():
    n = read_input()

def read_input():
    file = list(sys.stdin.read().split('\n'))
    chars = file[0].split()
    nbrOfChars = len(chars)
    scoress = file[1:nbrOfChars + 1]

    i = 0
    j = 0
    scores = {}
    for c1 in chars:
        scores[c1] = {}
        for c2 in chars:
            scores[c1][c2] = scoress[i][j]
            j += 1
    i += 1        
    print(scoress)

if __name__ == "__main__":
    main()
