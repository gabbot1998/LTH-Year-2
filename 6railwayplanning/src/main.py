import sys
import math

"""
graph is a nested dict where graph[u][v] returns (capacity, flow)
p_list is a list with priority of removals
edge_indices[i] gives edge(u,v) on index i
"""

def main():
    graph, p_list, edge_indices = read_input()
    



def read_input():
    N, M, C, P = list(map(int,sys.stdin.readline().split()))
    graph = {}
    edge_indices = []
    for i in range(M):
        u, v, c = list(map(int,sys.stdin.readline().split()))
        if u not in graph:
            graph[u] = {}
        graph[u][v] = (c,0) # Fill [u][v] with tuple (capacity, flow)
        edge_indices.append((u,v))

    p_list = []
    for i in range(P):
        p_list.append(list(map(int,sys.stdin.readline().split()))[0])

    return graph, p_list, edge_indices

if __name__ == "__main__":
    main()
