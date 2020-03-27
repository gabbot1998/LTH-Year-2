import sys

def main():
    file = sys.stdin.read().split()

    n = int(file[0])
    m = int(file[1])

    edges = file[2:]

if __name__ == "__main__":
    main()
