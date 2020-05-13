import sys
import math
from datetime import datetime

def main():
    scores, queries = read_input()
    

def read_input():
    file = list(sys.stdin.read().split('\n'))
    chars = file[0].split()
    nbrOfChars = len(chars)
    scoress = file[1:nbrOfChars + 1]
    nbrQueries = file[nbrOfChars + 1]
    arr = []
    newscore = []
    qrs = file[nbrOfChars + 2:-1]
    queries = []

    for q in qrs:
        q1 = q.split()
        queries.append((q1[0], q1[1]))

    for line in range(len(scoress)):
        newscore.append(list(map(int,scoress[line].split())))

    for line in scoress:
        arr.append(line.replace(" ", ""))

    i = 0
    j = 0
    scores = {}
    for c1 in chars:
        scores[c1] = {}
        for c2 in chars:
            scores[c1][c2] = newscore[i][j]
            j += 1
        i += 1
        j = 0

    return scores, queries


if __name__ == "__main__":
    main()
