import sys
from datetime import datetime

def main():
    file = list(map(int,sys.stdin.read().split()))

    n = file[0]
    m = file[1]

    edges = file[2:]
    #edges = file
    total_weight = 0

    trees = []
    added_to_trees = set()
    weight_list = []
    
    node_in_any_tree = [False] * (n+1)

    #graph[person] = [(person1, weight1), .. (personn, weightn)]

    a = datetime.now()
    for i in range(m):
        person1 = edges[3*i]
        person2 = edges[3*i + 1]
        weight = edges[3*i + 2]
        weight_list.append((person1, person2, weight))
#        if person1 not in added_to_trees:
#            trees.append({person1})
#            added_to_trees.add(person1)
#        if person2 not in added_to_trees:
#            trees.append({person2})
#            added_to_trees.add(person2)
    b = datetime.now()

    print("Making the weight list " + str(b-a))


    a = datetime.now()
    weight_list.sort(key = lambda list: list[2]) # Sort by weight
    b = datetime.now()
    print("Sorting the weight list " + str(b-a))
    #print(weight_list)
    a = datetime.now()
    for pair in weight_list:
        if len(trees) == 1 and len(trees[0]) == n: # If tree is complete
            break
        person1 = pair[0]
        person2 = pair[1]
        weight = pair[2]
        #print(person1,person2)
        #print(total_weight, weight)

        if node_in_any_tree[person1]:
            tree1, i1 = find_tree_containing(trees, person1)
            # If both trees are already added, merge trees
            if node_in_any_tree[person2]:
                tree2, i2 = find_tree_containing(trees, person2)
                if tree1 != tree2:
                    if i1 > i2:
                        del trees[i1]
                        del trees[i2]
                    if i2 > i1:
                        del trees[i2]
                        del trees[i1]
                    total_weight += weight
                    trees.append(tree1.union(tree2))
            # Else, add person2 to tree1
            else:
                trees[i1].add(person2)
                node_in_any_tree[person2] = True
                total_weight += weight
        # if person1 not in any tree
        else:
            # If person2 is in a tree, add person1 and set him to true
            if node_in_any_tree[person2]:
                tree2, i2 = find_tree_containing(trees, person2)
                trees[i2].add(person1)
                node_in_any_tree[person2] = True
                total_weight += weight
            # If no one is in a tree
            else:
                trees.append({person1,person2})
                node_in_any_tree[person1] = True
                node_in_any_tree[person2] = True
                total_weight += weight
        #print(node_in_any_tree,trees)
    """
        tree1, i1 = find_tree_containing(trees, person1)
        tree2, i2 = find_tree_containing(trees, person2)
        #print(tree1)
        #print(tree2)

        if len(trees) == 1:
            break

        else:
            if tree1 != tree2:
                if i1 > i2:
                    del trees[i1]
                    del trees[i2]
                if i2 > i1:
                    del trees[i2]
                    del trees[i1]
                    
                total_weight = total_weight + weight
                trees.append(tree1.union(tree2))
    """
    b = datetime.now()
    print("making the spanning tree " + str(b-a))
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
