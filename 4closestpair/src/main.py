import sys
import math
from datetime import datetime

def main():
    a = datetime.now()
    pairs, n = read_input()

    p_x = sorted(pairs,key = lambda x : x[0])
    p_y = sorted(pairs,key = lambda x : x[1])
    print(p_x)
    print(p_y)

    print(bruteforce(p_x, 0, n-1, n))

    # do stuff
    divide_and_conquer(p_x, 0, (n//2), n) # send left half
    divide_and_conquer(p_x, (n//2), n, n) # send right half




def divide_and_conquer(pairs, low, high, n):
    if n <= 3:
        return bruteforce(pairs, low, high, n)



def bruteforce(pairs, low, high, n):
    smallest_d = distance(pairs[low],pairs[high])
    for i in range(low,high):
        for j in range(low,high):
            if i != j:
                d = distance(pairs[i],pairs[j])
                print(i, j, pairs[i], pairs[j], d)
                if d < smallest_d and d != 0:
                    smallest_d = d
    return smallest_d


def distance(p1,p2):
    return math.sqrt(abs( math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) )) # TODO


def read_input():
    file = list(map(int,sys.stdin.read().split()))
    n = file[0]
    pairs = []
    for i in range(1,(n+1)):
        pairs.append((file[2*i-1], file[2*i]))
    return pairs, n

if __name__ == "__main__":
    main()
