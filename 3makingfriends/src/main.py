import sys

def main():
    file = list(map(int,sys.stdin.read().split()))

    n = file[0]
    m = file[1]

    edges = file[2:]
    total_weight = 0

    trees = []
    added_to_trees = set()
    weight_list = []



    #graph[person] = [(person1, weight1), .. (personn, weightn)]


    for i in range(m):
        person1 = edges[3*i]
        person2 = edges[3*i + 1]
        weight = edges[3*i + 2]
        weight_list.append((person1, person2, weight))
        if person1 not in added_to_trees:
            trees.append({person1})
            added_to_trees.add(person1)
        if person2 not in added_to_trees:
            trees.append({person2})
            added_to_trees.add(person2)




    weight_list.sort(key = lambda list: list[2])

    for pair in weight_list:
        person1 = pair[0]
        person2 = pair[1]
        weight = pair[2]
        tree1, i1 = find_tree_containing(trees, person1)
        tree2, i2 = find_tree_containing(trees, person2)
        #print(tree1)
        #print(tree2)

        if len(trees) != 1:
            if tree1 != tree2:
                trees.remove(tree1)
                trees.remove(tree2)
                #print("adding: " + str(weight))
                total_weight = total_weight + weight
                trees.append(tree1.union(tree2))

    print(total_weight)


def find_tree_containing(trees, person):
    i = -1
    #print(trees)
    for tree in trees:
        i = i + 1
        if person in tree:
            return (tree, i)
    return ({}, -1)

if __name__ == "__main__":
    main()
