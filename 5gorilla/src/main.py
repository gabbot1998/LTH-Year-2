import sys
import math
from datetime import datetime

def main():
    scores, queries = read_input()
    for query in queries:
        l_w1 = len(query[0])
        l_w2 = len(query[1])
        longest = max(l_w1, l_w2)
        A = [[None for col in range(l_w2+1)] for row in range(l_w1+1)] # One extra char for empty string

        sp, cost = opt(query,l_w1,l_w2,scores,A)
        print(sp[0] + " " + sp[1])
        #for line in A:
        #    print(line)


def opt(query,i,j,scores,A):
    #print()
    print(i,j)
    if A[i][j] != None: # Use what you already know
        return A[i][j]

    # Check if any is 0
    if i == 0:
        cost = j*scores['space'] # One will be zero ;)
        A[0][j] = (('*'*j,query[1][:j]),cost)
        return A[0][j]
    if j == 0:
        cost = i*scores['space'] # One will be zero ;)
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


def printValue(q, A, l_w1, l_w2):
    # print(q)
    s1 = ""
    s2 = ""
    q1r = q[0][::-1]
    q2r = q[1][::-1]
    # x = len(A)-1
    # y = len(A[0])-1
    # #Trying the reverse?
    # while x > 0 or y > 0:
    #     #print("pre x:{} y:{}".format(x, y))
    #     use_both = A[x-1][y-1]
    #     use_first = A[x-1][y]
    #     use_second = A[x][y-1]
    #
    #     best = max(use_both, use_first, use_second)
    #     if best == use_both:
    #         s1 = s1 +(q[0][x-1])
    #         s2 = s2 +(q[1][y-1])
    #         x-=1
    #         y-=1
    #     elif best == use_first:
    #         s1 = s1 +(q[0][x-1])
    #         s2 = s2 +('*')
    #         x-=1
    #     elif best == use_second:
    #         s1 = s1 +('*')
    #         s2 = s2 +(q[1][y-1])
    #         y-=1
    #     print(s1[::-1],s2[::-1])
    # s1 = s1[::-1] #reverse string
    # s2 = s2[::-1]
    x=len(q1r)-1
    y=len(q2r)-1
    ## FIRST ENTRY
    # use_both = A[x][y]
    # use_first = A[x-1][y]
    # use_second = A[x][y-1]
    # best = max(use_both, use_first, use_second)
    # if best == use_both:
    #     s1 = s1 +(q[0][x-1])
    #     s2 = s2 +(q[1][y-1])
    #     x-=1
    #     y-=1
    # elif best == use_first:
    #     s1 = s1 +(q[0][x-1])
    #     s2 = s2 +('*')
    #     x-=1
    # elif best == use_second:
    #     s1 = s1 +('*')
    #     s2 = s2 +(q[1][y-1])
    #     y-=1
    # print(s1[::-1],s2[::-1])
    while x > 0 or y > 0:
        # print("pre x:{} y:{}".format(x, y))

        if x+1 < len(A) and y-1 < len(A[0]): use_both = A[x-1][y-1]
        if x+1 < len(A): use_first = A[x-1][y]
        if y+1 < len(A[0]): use_second = A[x][y-1]

        best = max(use_both, use_first, use_second)
        if best == use_both:
            s1 = s1 +(q[0][x-1])
            s2 = s2 +(q[1][y-1])
            x-=1
            y-=1
        elif best == use_first:
            s1 = s1 +(q[0][x-1])
            s2 = s2 +('*')
            x-=1
        elif best == use_second:
            s1 = s1 +('*')
            s2 = s2 +(q[1][y-1])
            y-=1
        # print(s1[::-1],s2[::-1])
        # print(x,y)
    s1 = s1[::-1] #reverse string
    s2 = s2[::-1]
    print(s1 + " " + s2)


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
