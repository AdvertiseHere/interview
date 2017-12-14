# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree
# connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:


#     {'A': [('B', 2)],
#      'B': [('A', 2), ('C', 5)],
#      'C': [('B', 5)]}

# Vertices are represented as unique strings. The function definition should be question3(G)


def question3(G):
    vertices = G.keys()

    edges = set()
    for i in vertices:
        for j in G[i]:
            edge = (j[1], i, j[0])
            edge_from = (j[1], j[0], i)
            if i > j[0]:
                edges.add(edge_from)
            elif i < j[0]:
                edges.add(edge)


    edges = sorted(list(edges))


    filtered_edges = []
    vertices = [set(i) for i in vertices]

    for i in edges:
        for j in xrange(len(vertices)):
            if i[1] in vertices[j]:
                index1 = j
                print index1
            if i[2] in vertices[j]:
                index2 = j

        if index1 < index2:
            vertices[index1] = set.union(vertices[index1], vertices[index2])
            vertices.pop(index2)
            filtered_edges.append(i)

        elif index2 < index1:
            vertices[index2] = set.union(vertices[index1], vertices[index2])
            vertices.pop(index1)
            filtered_edges.append(i)


    minimum_spanning_tree = {} # your resulting adjacency lists, one for each vertex in the graph
    for weight, u, v in filtered_edges:
        if u not in minimum_spanning_tree:
            minimum_spanning_tree[u] = []

        minimum_spanning_tree[u].append((v, weight))

        if v not in minimum_spanning_tree:
            minimum_spanning_tree[v] = []

        minimum_spanning_tree[v].append((u, weight))

    print minimum_spanning_tree

    # sort edges by weight



def main():
    return question3({'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]})


if __name__ == "__main__":
    main()
