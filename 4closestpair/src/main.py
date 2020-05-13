import sys
import math
from datetime import datetime

def main():
    a = datetime.now()
    pairs, n = read_input()

    p_x = sorted(pairs,key = lambda x : x[0])
    #p_y = sorted(pairs,key = lambda x : x[1])
    #print(p_x)
    #print(p_y)

    print("{0:0.6f}".format(divide_and_conquer(p_x, 0, n-1)))
    b = datetime.now()

    #print("Total time: {}".format(b - a))
    # do stuff
    #divide_and_conquer(p_x, 0, (n//2), n) # send left half
    #divide_and_conquer(p_x, (n//2), n, n) # send right half




def divide_and_conquer(pairs, low, high):
    #print("low {} high {} points {}".format(low,high,pairs[low:high]))
    midline = ((high - low) // 2) + low
    n = high - low
    if n < 3:
        return bruteforce(pairs, low, high)
    else:
        delta = min(divide_and_conquer(pairs, low, midline),
                    divide_and_conquer(pairs, midline + 1, high))

        # Find points left and right of midline (delta distance)
        s_y = []
        i = midline - 1
        s_y.append(pairs[midline])

        while i >= low and ((pairs[midline][0] - pairs[i][0]) <= delta):  #Look left
            s_y.append(pairs[i])
            i -= 1

        i = midline + 1
        while i <= high and ((pairs[i][0] - pairs[midline][0]) <= delta): #Look right
            s_y.append(pairs[i])
            i += 1

        s_y.sort(key=lambda x : x[1])
        # s_right.sort(key=lambda x : x[1])
        #print("S_y be like: {}".format(s_y))
        # print("Sr be like: {}".format(s_right))
        d = min(check_midline(s_y, delta), delta)

        return d



def check_midline(s_y, delta):
    size = len(s_y)
    min_d = delta
    max = 0
    min = 0
    for i in range(size - 1):
        if size < i + 6:
            max = size
        else:
            max = i + 6
        for j in range(i + 1, max):
            d = distance(s_y[i], s_y[j])
            if d < min_d:
                min_d = d
            else:
                break
    return min_d

def bruteforce(pairs, low, high):
    smallest_d = distance(pairs[low],pairs[high])
    for i in range(low,high):
        for j in range(low,high):
            if i != j:
                d = distance(pairs[i],pairs[j])
                #print("BRUTE")
                #print(i, j, pairs[i], pairs[j], d)
                if d < smallest_d and d != 0:
                    smallest_d = d
    return smallest_d


def distance(p1,p2):
    return math.sqrt(abs( math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))) # TODO


def read_input():
    file = list(map(int,sys.stdin.read().split()))
    n = file[0]
    pairs = []
    for i in range(1,(n+1)):
        pairs.append((file[2*i-1], file[2*i]))
    return pairs, n

if __name__ == "__main__":
    main()
