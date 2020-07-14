from util import Stack
'''
Thoughts:

I think we want depth first.
We start with an input child, and must trace back via parents to find the farthest ancestor
Is this reversed?
It's recursive!! takes in a dataset and an ID
Need to know when a child doesn't have a parent- that's our base case. That's the root ancestor

Let's think through how to make a helper function that finds our parents.

Use a stack if I don't do recursion

'''


def find_parents(child, ancestors):
    # we need the [0] element in the tuple where child is [1]
    # need to unpack the tuple?
    parents = set()
    print(parents, "beginning of helper func")

    for par, chi in ancestors:
        if chi == child:
            parents.add(par)
            print(parents, "inside helper func")

    print(parents, "end of helper func")
    return parents


def earliest_ancestor(ancestors, starting_node):
    pass

    s = Stack()

    s.push(starting_node)

    visited = set()
    # ancest = set()

    while s.size() > 0:

        current_node = s.pop()

        # need to return last_node somewhere

        if current_node not in visited:
            visited.add(current_node)
            # then we get current_node's parents
            parents = find_parents(current_node, ancestors)

            if s.size() == 0 and len(parents) == 0:
                if current_node == starting_node:
                    return -1
                else:
                    print(current_node, "answer!")
                    return current_node

            print(parents, "inside earliest_ancestor")

            # check if parents is None/empty set, what then?
            if len(parents) > 0:
                for parent in parents:
                    print(parent, "inside for loop")
                    s.push(parent)

        if s.size() > 1 and len(parents) == 0:
            continue
