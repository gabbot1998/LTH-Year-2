import sys
import math
from datetime import datetime
import sys
sys.setrecursionlimit(5000)


def main():
    scores, queries = read_input()
    for query in queries:
        l_w1 = len(query[0])
        l_w2 = len(query[1])
        longest = max(l_w1, l_w2)
        A = [[None for col in range(l_w2+1)] for row in range(l_w1+1)] # One extra char for empty string
        ##print(l_w1, l_w2)
        ##print("Query: {} \nA: {}".format(query,A))
        #print(scores)
        opt(query,l_w1,l_w2,scores,A)
        #print(A)

        printValue(scores, query,A, l_w1 - 1, l_w2 - 1)

def printValue(score, q, A, l_w1, l_w2):
    s1 = ""
    s2 = ""
    x = l_w1+1
    y = l_w2+1
    while x != 0 or y != 0:
        #print(s1,s2)
        #print(x,y)
        use_both = A[x-1][y-1] + score[q[0][x-1]][q[1][y-1]]
        use_first = A[x-1][y] + score['space']
        use_second = A[x][y-1] + score['space']

        currentScore = A[x][y]
        if currentScore == use_both:
            s1 = (q[0][x-1]) + s1
            s2 = (q[1][y-1]) + s2
            x-=1
            y-=1
        elif currentScore == use_first:
            s1 = (q[0][x-1]) + s1
            s2 = ('*') + s2
            x-=1
        elif currentScore == use_second:
            s1 = ('*') + s1
            s2 = (q[1][y-1]) + s2
            y-=1
    print(s1 + " " + s2)


def opt(query,i,j,scores,A):
    ##print()
    #print(i,j,A)
    if A[i][j] != None: # Use what you already know
        cw1 = query[0][i - 1]
        cw2 = query[1][j - 1]
        ##print("FOUND value for i:{} j:{} cw1:{}, cw2:{}  ".format(i,j,cw1,cw2))
        return A[i][j]

    # Check if any is 0
    if i == 0:
        cost = j*scores['space'] # One will be zero ;)
        ##print("ZERO value for i:{} j:{}, cost: {}".format(i,j,cost))
        A[0][j] = cost
        return cost

    if j == 0:
        cost = i*scores['space'] # One will be zero ;)
        ##print("ZERO value for i:{} j:{}, cost: {}".format(i,j,cost))
        A[i][0] = cost
        return cost

    cw1 = query[0][i - 1]
    cw2 = query[1][j - 1]

    # The real stuff
    #print(cw1, cw2)
    a = scores[cw1][cw2] + opt(query, (i-1), (j-1), scores, A)
    #print("updating (i{}),(j{}) to {}".format(i,j,(A[i-1][j-1]) + scores[cw1][cw2]))
    b = scores['space'] + opt(query, (i-1), (j), scores, A)
    #print("updating (i{}),(j{}) to {}".format(i,j,A[i-1][j]))
    c = scores['space'] + opt(query, (i), (j-1), scores, A)
    #print("updating (i{}),(j{}) to {}".format(i,j,A[i][j - 1]))

    A[i][j] = max([a, b, c])
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
