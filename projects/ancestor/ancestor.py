
def find_parents(child):
    pass


def earliest_ancestor(ancestors, starting_node):
    pass


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
