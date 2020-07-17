import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        friendships = []

        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)

        # shuffle that- shuffles in place
        self.fisher_yates_shuffle(friendships)
        # take as many as we need
        total_friendships = num_users * avg_friendships
        random_friendships = friendships[:total_friendships//2]

        # add to self.friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def linear_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # as long as we haven't made all the friendships we need
        target_number_friendships = num_users * avg_friendships
        friendships_created = 0
        while friendships_created < target_number_friendships:
            # pick 2 random numbers between 1 and the last id
            friend_one = random.randint(1, num_users + 1)
            friend_two = random.randint(1, num_users + 1)

        # try to create that friendship
            friendship_was_made = self.add_friendship(friend_one, friend_two)
        # if it works, then increment friendship counter
            if friendship_was_made:
                friendships_created += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        Nodes are people. 
        Edges are relationships.
        Must trace the shortest path.
        Sounds like a BFS to me. Use a Queue class here. 

        key is the friend node, value is all the nodes between them and friend.
        Does the path include the friend node? No- directions say "between"
        Tracing the entire existing network, 
            first gen node is visited, added as key with empty path
            second gen node is visited, added as key with path to it as value
            third gen node is visited, added as key with path to it as value
            etc.
        Every node gets visited, every node gets placed as a key.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # node1 : []
        # node2 : [node1]
        # node3 : [node1, node2]
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            current_node = path[-1]

            if current_node not in visited:
                visited[current_node] = path

                friendships = self.friendships[current_node]
                # need friendships of the user id. need get neighbors
                # print(friendships, "friendships")

                # iterate over friendships
                for friend in friendships:
                    new_path = list(path)
                    new_path.append(friend)
                    q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    # print(sg.friendships)

    sg.linear_populate_graph(1000, 5)

    # connections = sg.get_all_social_paths(1)
    # print(connections, 'answer')

    # what percentage of total users are in our extended social network?

    # how many people we know, divided by how many people there are

    # print(f'{(len(connections) - 1) / 1000 * 100}%')

    # what is the average degree of separation between a user and those in his/her extended network?
    # need the average length of a path to each user
    # traverse a user's extended connections, gatehr lengths, sum,
    # divide by number of friends in connected components aka social connections
    # total_lengths = 0
    # for friend in connections:
    #     total_lengths += len(connections[friend])

    # print(f' Average degree of separation: {total_lengths / len(connections)}')
