import sys
from datetime import datetime

def main():
    file = list(map(int,sys.stdin.read().split()))

    n = file[0]
    m = file[1]

    edges = file[2:]
    #edges = file
    total_weight = 0

    trees = set() 
    added_to_trees = set()
    weight_list = []



    #graph[person] = [(person1, weight1), .. (personn, weightn)]

    a = datetime.now()
    for i in range(m):
        person1 = edges[3*i]
        person2 = edges[3*i + 1]
        weight = edges[3*i + 2]
        weight_list.append((person1, person2, weight))
        if person1 not in added_to_trees:
            trees.add(frozenset({person1}))
            added_to_trees.add(person1)
        if person2 not in added_to_trees:
            trees.add(frozenset({person2}))
            added_to_trees.add(person2)
    b = datetime.now()

    print("Making the weight list " + str(b-a))


    a = datetime.now()
    weight_list.sort(key = lambda list: list[2])
    b = datetime.now()
    print("Sorting the weight list " + str(b-a))

    a = datetime.now()
    for pair in weight_list:
        person1 = pair[0]
        person2 = pair[1]
        weight = pair[2]
        tree1 = find_tree_containing(trees, person1)
        tree2 = find_tree_containing(trees, person2)
        #print(tree1)
        #print(tree2)
        #print(trees)
        #print("")

        if len(trees) == 1:
            break

        else:
            if tree1 != tree2:
                trees.remove(tree1)
                trees.remove(tree2)
                    
                total_weight = total_weight + weight
                trees.add(tree1.union(tree2))

    b = datetime.now()
    print("making the spanning tree " + str(b-a))
    print(total_weight)


def find_tree_containing(trees, person):
    #print(trees)
    for tree in trees:
        if person in tree:
            return tree
    return {}

if __name__ == "__main__":
    main()
