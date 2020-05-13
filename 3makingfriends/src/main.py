import sys
from datetime import datetime

def main():
    file = list(map(int,sys.stdin.read().split()))

    n = file[0]
    m = file[1]

    edges = file[2:]
    total_weight = 0


    weight_list = []
    parents = {}
    size = {}



    a = datetime.now()
    for i in range(m):
        person1 = edges[3*i]
        person2 = edges[3*i + 1]
        weight = edges[3*i + 2]
        weight_list.append((person1, person2, weight))
        if person1 not in parents:
            makeSet(person1, parents, size)
        if person2 not in parents:
            makeSet(person2, parents, size)
    b = datetime.now()


    a = datetime.now()
    weight_list.sort(key = lambda list: list[2])
    b = datetime.now()

    a = datetime.now()
    for pair in weight_list:

        person1 = pair[0]
        person2 = pair[1]
        weight = pair[2]
        tree1 = find(person1, parents)
        tree2 = find(person2, parents)

        if size[tree1] == n or size[tree2] == n:
            break

        elif tree1 != tree2:
            old_weight = total_weight
            total_weight = total_weight + weight
            union(person1, person2, size, parents)

    b = datetime.now()
    print(total_weight)



def union(u, v, size, parents):
    u = find(u, parents)
    v = find(v, parents)
    if size[u] > size[v]:
        parents[v] = u
        size[u] = size[u] + size[v]
    elif size[u] < size[v]:
        parents[u] = v
        size[v] = size[u] + size[v]
    elif u != v:
        parents[v] = u
        size[u] = size[u] + size[v]


def find(node, parents):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node], parents)
        return parents[node]

def makeSet(node, parents, size):
    parents[node] = node
    size[node] = 1

if __name__ == "__main__":
    main()
