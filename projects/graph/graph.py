"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import pprint


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        # should return neighbors. does it return a list or set of them?

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # step one make a queue
        q = Queue()
        # what do we put in it? enqueue starting_vertex
        q.enqueue(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our queue isn't empty
        while q.size() > 0:
            # dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
        # if we haven't visited this node yet,
            if current_node not in visited:
                # then mark as visited
                print(current_node)
                visited.add(current_node)
        # print node
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors, enqueue their neighbors
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use a stack here
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we've bee here before
        visited = set()
        # while our stack isn't empty
        while s.size() > 0:
            # pop off whatever's on top, this is our current_node
            current_node = s.pop()
        # if we haven't visited this node before
            if current_node not in visited:
                print(current_node)
        # mark as visited
                visited.add(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)

        # for each of the neighbors
                for neighbor in neighbors:
                    # push them to our stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case is where there are no more neighbors
        # where does it call itself?
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # need a queue
        q = Queue()
        # enqueue our starting_vertex
        q.enqueue([starting_vertex])
        # create set to track visited verts
        visited = set()

        # while our queue is not empty
        while q.size():
            # current node is dequeued off of queue
            current_node_list = q.dequeue()
            last_node = current_node_list[-1]

        # check to see if current_node matches detination_vert
            if last_node == destination_vertex:
                # if yes, return it
                return current_node_list

        # if current_node not in visited
            if last_node not in visited:
                # add to visited
                visited.add(last_node)
        # get its neighbors
                neighbors = self.get_neighbors(last_node)
        # for each neighbor
                for neighbor in neighbors:
                    # enqueue by making a shallow copy so we don't mutate the original path
                    node_list = list(current_node_list)
                    node_list.append(neighbor)
                    q.enqueue(node_list)

                    # could be written this way
                    #q.enqueue(current_node_list + [neighbor])

        # return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            current_node = s.pop()
            last_node = current_node[-1]

            if last_node == destination_vertex:
                return current_node

            if last_node not in visited:
                visited.add(last_node)
                neighbors = self.get_neighbors(last_node)

                for neighbor in neighbors:
                    dfs_list = list(current_node)
                    dfs_list.append(neighbor)
                    s.push(dfs_list)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=list()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if visited is None:
        #     visited = set()

        # if path is None:
        #     path = []

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            new_path = list(path)

            new_path.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return new_path

            for neighbor in self.get_neighbors(starting_vertex):
                result = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                # have to wait until stack finishes with all the recursive calls, then you can return the result
                if result:
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6), "bfs_simple")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6), "dfs_simple")
    print(graph.dfs_recursive(1, 6), "dfs_rec")
