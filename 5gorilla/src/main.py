import sys
import math
import numpy as np
from datetime import datetime
import sys
sys.setrecursionlimit(1500)

def main():
    scores, queries = read_input()
    for query in queries:
        l_w1 = len(query[0])
        l_w2 = len(query[1])
        longest = max(l_w1, l_w2)
        A = [[None for col in range(l_w2+1)] for row in range(l_w1+1)] # One extra char for empty string
        #A = np.empty([l_w1 +1, l_w2+1], dtype=object) ### replaced list with np array for faster insertion

        sp, cost = opt(query,l_w1,l_w2,scores,A)
        print(sp[0] + " " + sp[1])


def opt(query,i,j,scores,A):
    if A[i][j] != None: # Use what you already know
        # print("found")
        return A[i][j]

    # Check if any is 0
    if i == 0:
        cost = j*scores['space']
        A[0][j] = (('*'*j,query[1][:j]),cost)
        return A[0][j]
    if j == 0:
        cost = i*scores['space']
        A[i][0] = ((query[0][:i],'*'*i),cost)
        return A[i][0]

    cw1 = query[0][i - 1]
    cw2 = query[1][j - 1]

    # The real stuff
    sp1, score1 = opt(query, (i-1), (j-1), scores, A)
    a = scores[cw1][cw2] + score1

    sp2, score2 = opt(query, (i-1), (j), scores, A)
    b = scores['space'] + score2

    sp3, score3 = opt(query, (i), (j-1), scores, A)
    c = scores['space'] + score3
    biggest = max([a, b, c])
    if a == biggest:
        A[i][j] = ((sp1[0] + query[0][i - 1], sp1[1] + query[1][j - 1]), a)
        return A[i][j]
    elif b == biggest:
        A[i][j] = ((sp2[0] + query[0][i - 1], sp2[1] + '*'), b)
        return A[i][j]
    elif c == biggest:
        A[i][j] = ((sp3[0] + '*', sp3[1] + query[1][j - 1]), c)
        return A[i][j]

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
    scores['space'] = -4

    return scores, queries


if __name__ == "__main__":
    main()
