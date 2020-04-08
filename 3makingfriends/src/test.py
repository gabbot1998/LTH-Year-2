parents = {}
size = {}

def union(u, v, size, parents):
    u = find(u, parents)
    v = find(v, parents)
    if size[u] < size[v]:
        parents[u] = v
        size[v] = size[u] + size[v]
    elif size[u] > size[v]:
        parents[v] = u
        size[u] = size[u] + size[v]
    elif u != v:
        parents[v] = u
        size[u] = size[u] + 1

def find(node, parents):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node], parents)
        return parents[node]

def makeSet(node, parents, size):
    parents[node] = node
    size[node] = 0

makeSet("Mahir", parents, size)
makeSet("Gabriel", parents, size)
