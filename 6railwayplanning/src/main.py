import sys
import math
from queue import Queue

"""
graph is a nested dict where graph[u][v] returns (capacity, flow)
p_list is a list with priority of removals
edge_indices[i] gives edge(u,v) on index i
"""

def main():
    graph, p_list, edge_indices, target, required_capacity = read_input()

    do_flow(graph, target)
    printgraph(graph)
    #print(get_max_cap(graph))
    old_max = 0
    for i in range(len(p_list)):
        u_rem, v_rem = edge_indices[p_list[i]]
        del graph[u_rem][v_rem]
        print("\nREMOVAL {}: removing ({} {})".format(i, u_rem, v_rem))

        do_flow(graph, target)
        printgraph(graph)

        max = get_max_cap(graph)
        print(max)
        if max < required_capacity:
            print(i+1, old_max)
            break
        old_max = max

def do_flow(graph, target):
    path, delta = bfs(graph, target)
    while delta != 0:
        increase_flow(path, delta, graph, target)
        path, delta = bfs(graph, target)

def get_max_cap(graph):
    max = 0
    for val in graph[0].keys():
        max = max + graph[0][val][0]
    return max


def read_input():
    N, M, C, P = list(map(int,sys.stdin.readline().split()))
    graph = {}
    edge_indices = []
    for i in range(M):
        u, v, c = list(map(int,sys.stdin.readline().split()))
        if u not in graph:
            graph[u] = {}

        graph[u][v] = (c, 0) # Fill [u][v] with tuple (capacity, flow)
        edge_indices.append((u,v))

    p_list = []
    for i in range(P):
        p_list.append(list(map(int,sys.stdin.readline().split()))[0])

    return graph, p_list, edge_indices, N-1, C


def increase_flow(path, delta, graph, target):
    current_node = target
    previous = path[current_node]
    while True:
        #print(current_node)
        cap, flow = graph[previous][current_node]
        graph[previous][current_node] = (cap, flow + delta)
        current_node = previous
        if current_node in graph[previous]:
            cap, flow_b = graph[previous][current_node]
            graph[previous][current_node] = (cap + delta, flow_b)
        elif current_node != previous:
            #print("creating back edge from: {}, to: {}".format(previous,current_node))
            graph[previous][current_node] = (flow, 0)
        if previous == 0:
            break
        previous = path[previous]
    #print(graph)



def bfs(graph, target): #Returns a list of the path and the minimum flow we can increase.
    current_node = 0
    pred = {}

    queue = Queue()
    queue.put(current_node)
    visited = set()
    min_delta = sys.maxsize
    while not queue.empty():
        current_node = queue.get()
        for neighbor in graph[current_node]:
            cap, flow = graph[current_node][neighbor]
            if neighbor not in visited and cap - flow != 0:
                visited.add(neighbor)
                queue.put(neighbor)
                pred[neighbor] = current_node
                cap, flow = graph[current_node][neighbor]
                delta = cap - flow
                if delta < min_delta:
                    min_delta = delta

                if neighbor == target:
                    return pred, min_delta
    #print("No path")
    return {}, 0

def printgraph(graph):
    for key in graph:
        print("Edges from {}".format(key))
        print(graph[key])

if __name__ == "__main__":
    main()
