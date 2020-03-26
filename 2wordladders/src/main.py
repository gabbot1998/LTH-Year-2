import sys

def main():
    file = sys.stdin.read().split()

    n = int(file[0])
    q = int(file[1])

    del file[:2]

    build_graph(file,n,q)
    print()
    read_queries(file,n,q)

def build_graph(file,n,q):
    for i in range(n):
        # TODO: Load to graph
        print(file[i])

def read_queries(file,n,q):
    for i in range(q):
        # TODO: Do something with queries (search!)
        start_word = file[n + 2*i]
        end_word = file[n + 2*i +1]
        print(start_word + " " + end_word)

if __name__ == "__main__":
    main()
