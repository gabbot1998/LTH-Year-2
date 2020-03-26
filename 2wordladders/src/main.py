import sys
from queue import Queue
from datetime import datetime

def main():
    file = sys.stdin.read().split()

    n = int(file[0])
    q = int(file[1])
    words = file[2:n+2]
    queries = file[n+2:]

    graph = build_graph(words,n,q)
    #print(graph)
    #print()
    read_queries(graph,queries,n,q)

def build_graph(words,n,q):
    graph = {}
    for word in words:
        # TODO: Load to graph
        graph[word] = (False, get_edges(words, word))
    return graph

# Searches for words that conform and returns arcs
def get_edges(words,word):
    edges = []
    for comp_word in words:
        if word != comp_word and conforms(word, comp_word):
            edges.append(comp_word)

    return edges

# Checks if comp_word conforms to rule
def conforms(word, comp_word):
    word = word[1:] # First char not needed
    comp_word = [c for c in comp_word] # Remake to [chars]
    for c_1 in word:
        n_letters = len(comp_word)
        for i in range(n_letters):
            # If we found it, good, del and move on
            if c_1 == comp_word[i]:
                del comp_word[i]
                break

        # If we have not deleted one letter, return False!
        if len(comp_word) == n_letters:
            return False
    return True

def read_queries(graph,queries,n,q):
    for i in range(q):
        # TODO: Do something with queries (search!)
        start_word = queries[2*i]
        target_word = queries[2*i +1]

        if start_word == target_word:
            print(0)
            continue

        distance = bfs(graph, start_word, target_word)
        if distance >= 0:
            print(distance)
        else:
            print("Impossible")


        #print(start_word + " " + end_word)

def bfs(graph, start_word, target):
    pred = {}
    graph_copy = graph.copy()

    queue = Queue()
    queue.put(start_word)

    while not queue.empty():
        current_word = queue.get()
        current_edges = graph_copy[current_word][1]

        for neighbor in current_edges:
            if not graph_copy[neighbor][0]: #If the neighbor is not visited
                graph_copy[neighbor] = (True, graph_copy[neighbor][1]) #Set the neighbor as visited
                queue.put(neighbor)
                pred[neighbor] = current_word
                if neighbor == target:
                    #print(pred)
                    return get_distance(pred, start_word, target)
    return -1

def get_distance(pred, start_word, current_word):
    #print(current_word)
    if current_word == start_word:
        return 0
    else:
        return 1 + get_distance(pred, start_word, pred[current_word])



if __name__ == "__main__":
    main()
