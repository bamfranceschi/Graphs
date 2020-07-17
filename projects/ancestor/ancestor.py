from util import Stack
from util import Queue
'''
Thoughts:

I think we want depth first.
We start with an input child, and must trace back via parents to find the farthest ancestor
Is this reversed?
It's recursive!! takes in a dataset and an ID
Need to know when a child doesn't have a parent- that's our base case. That's the root ancestor

Let's think through how to make a helper function that finds our parents.

Use a stack if I don't do recursion

Translate problem
- Nodes: people
- Edges: when a child has a parent

Build our graph or just define get_neighbors

Chose algorithm
-either bfs or dfs
-going with dfs
-how would we know if dfs happened to be faster?

'''


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


# def find_parents(child, ancestors):
#     # we need the [0] element in the tuple where child is [1]
#     # need to unpack the tuple?
#     parents = set()
#     print(parents, "beginning of helper func")

#     for par, chi in ancestors:
#         if chi == child:
#             parents.add(par)
#             print(parents, "inside helper func")

#     print(parents, "end of helper func")
#     return parents


# let's build a path like we did in search
# but we don't know when to stop until we've seen everyone


def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()

    visited = set()

    s.push([starting_node])

    longest_path = [starting_node]
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        # if path is longer, or path is equal but the id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)

    return aged_one
    # s = Stack()

    # s.push(starting_node)

    # visited = set()
    # # ancest = set()

    # while s.size() > 0:

    #     current_node = s.pop()

    #     # need to return last_node somewhere

    #     if current_node not in visited:
    #         visited.add(current_node)
    #         # then we get current_node's parents
    #         parents = find_parents(current_node, ancestors)

    #         if s.size() == 0 and len(parents) == 0:
    #             if current_node == starting_node:
    #                 return -1
    #             else:
    #                 print(current_node, "answer!")
    #                 return current_node

    #         print(parents, "inside earliest_ancestor")

    #         # check if parents is None/empty set, what then?
    #         if len(parents) > 0:
    #             for parent in parents:
    #                 print(parent, "inside for loop")
    #                 s.push(parent)

    #     if s.size() > 1 and len(parents) == 0:

    #         continue
