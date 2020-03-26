import sys

def main():
    file = sys.stdin.read().split()

    n = int(file[0])
    q = int(file[1])
    words = file[2:n+2]
    queries = file[n+2:]
    graph = {}

    build_graph(graph,words,n,q)
    print()
    read_queries(graph,queries,n,q)

def build_graph(graph,words,n,q):
    for word in words:
        # TODO: Load to graph
        print(word)
        graph[word] = (False,[])

# Searches for words that conform and returns arcs
def get_edges(words,word):
    edges = []
    for comp_word in words:
        if conforms(word, comp_word):
            edges.append(comp_word)

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
        end_word = queries[2*i +1]
        print(start_word + " " + end_word)

if __name__ == "__main__":
    main()
