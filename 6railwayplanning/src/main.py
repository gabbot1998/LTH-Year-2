import sys
from queue import Queue

"""
graph is a nested dict where graph[u][v] returns (capacity, flow)
"""

def main():
    graph, p_list, target, required_capacity = read_input()
    # Graph is now completed. We want to remove all removables.
    remove_edges(graph, p_list)

    # Check if we can fulfill it with all removed
    do_flow(graph, target)
    max_cap = get_max_cap(graph)
    if max_cap > required_capacity:
        print(len(p_list)-1, max_cap)
        return

    # How many edges do we have to add to get to required_capacity?
    for i in range(len(p_list) -1, -1, -1):    #(start from len, go to 0, inc is -1)
        # Build edge
        u, v, c = p_list[i]
        add_edge(graph, u, v, c)

        # Do one iteration and check if we fill required_capacity
        do_flow(graph, target)
        max_cap = get_max_cap(graph)
        if max_cap >= required_capacity:
            print(i, max_cap)
            break

def do_flow(graph, target):
    path, delta = bfs(graph, target)
    while delta != 0:
        increase_flow(path, delta, graph, target)
        path, delta = bfs(graph, target)

def get_max_cap(graph):
    max_cap = 0
    for val in graph[0].keys():
        max_cap = max_cap + graph[0][val][1]
    return max_cap

def remove_edges(graph, p_list):
    for i in range(len(p_list)):
        u, v, _ = p_list[i]
        del graph[u][v]
        del graph[v][u]

def add_edge(graph, u, v, c):
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = (c, 0) # Fill [u][v] with tuple (capacity, flow)
    graph[v][u] = (c, 0) # bidirectional

def read_input():
    N, M, C, P = list(map(int, sys.stdin.readline().split()))
    edge_indices = []
    graph = {}
    for i in range(M):
        u, v, c = list(map(int, sys.stdin.readline().split()))
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = (c, 0) # Fill [u][v] with tuple (capacity, flow)
        graph[v][u] = (c, 0) # bidirectional
        edge_indices.append((u, v, c))

    p_list = []
    for i in range(P):
        index = list(map(int, sys.stdin.readline().split()))[0]
        p_list.append(edge_indices[index])

    return graph, p_list, N-1, C


def increase_flow(path, delta, graph, target):
    v = target
    u = path[v]
    while True:
        cap, flow = graph[u][v] # increase flow with delta
        graph[u][v] = (cap, flow + delta)

        _, flow_b = graph[v][u]
        graph[v][u] = (flow + delta, flow_b)

        if u == 0:
            break
        v = u
        u = path[v]

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
    return {}, 0

def printgraph(graph):
    for key in graph:
        print("Edges from {}".format(key))
        print(graph[key])

if __name__ == "__main__":
    main()
