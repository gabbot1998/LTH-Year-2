import sys
import math
from datetime import datetime

def main():
    scores, queries = read_input()
    for query in queries:
        l_w1 = len(query[0])
        l_w2 = len(query[1])
        A = [[None for col in range(l_w2+1)] for row in range(l_w1+1)] # One extra char for empty string
        #print(l_w1, l_w2)
        #print("Query: {} \nA: {}".format(query,A))
        print(A)
        print(opt(query,l_w1,l_w2,scores,A))

        testScores = {'A': {}, }
    #print(scores, queries)


def opt(query,i,j,scores,A):
    print()
    print(i,j,A)
    if A[i][j] != None: # Use what you already know
        cw1 = query[0][i - 1]
        cw2 = query[1][j - 1]
        print("FOUND value for i:{} j:{} cw1:{}, cw2:{}  ".format(i,j,cw1,cw2))
        return A[i][j]

    # Check if any is 0
    if i == 0 or j == 0:
        cost = i*scores['space'] + j*scores['space'] # One will be zero ;)
        print("ZERO value for i:{} j:{}, cost: {}".format(i,j,cost))
        A[i][j] = cost
        return cost

    cw1 = query[0][i - 1]
    cw2 = query[1][j - 1]

    # The real stuff
    print(cw1, cw2)
    A[i][j] = scores[cw1][cw2] + opt(query, (i-1), (j-1), scores, A)
    print("updating (i{}-1),(j{}-1) to {}".format(i,j,A[i-1][j-1]))
    A[i][j] = scores['space'] + opt(query, (i-1), (j), scores, A)
    print("updating (i{}-1),(j{}) to {}".format(i,j,A[i-1][j]))
    A[i][j] = scores['space'] + opt(query, (i), (j-1), scores, A)
    return max([A[i-1][j-1], A[i-1][j], A[i][j-1]])

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
