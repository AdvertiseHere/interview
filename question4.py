# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an ancestor
#  of both nodes. For example, the root is a common ancestor of all nodes on the tree,
#   but if both nodes are descendents of the root's left child, then that left child
#   might be the lowest common ancestor. You can assume that both nodes are in the tree,
#    and the tree itself adheres to all BST properties. The function definition should
#    look like question4(T, r, n1, n2), where T is the tree represented as a matrix,
#    where the index of the list is equal to the integer stored in that node and a 1
#    represents a child node, r is a non-negative integer representing the root, and n1
#    and n2 are non-negative integers representing the two nodes in no particular order.
#    For example, one test case might be

def question4(T, r, n1, n2):
    n1_parents = []
    n2_parents = []
    if n1 == r or n2 == r:
        return r
    else:
        while n1 != r:
            n1 = parent(T, n1)
            n1_parents.append(n1)


        while n2 != r:
            n2 = parent(T, n2)
            n2_parents.append(n2)
            print n2_parents
            if n2 in n1_parents:
                return n2


    return -1

# We know that in our adjacency matrix, a "1" value indicates a child node. That means any node
# containing one or more "1" values is a parent.
def parent(T, node):
    for i in range(len(T)):
        if T[i][node] == 1:
            return i
    return -1


print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,4,1)
