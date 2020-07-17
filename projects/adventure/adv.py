from room import Room
from player import Player
from world import World
from util import Stack
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# # have to build the graph as we go
visited = {}
reverse = {"n": "s", "e": "w", "s": "n", "w": "e"}
visited[player.current_room.id] = player.current_room.get_exits()
best_path = []

while len(visited) < len(room_graph) - 1:
    # check if current room is in dict
    if player.current_room.id not in visited:
        # if not:
        # add current room to visited
        visited[player.current_room.id] = player.current_room.get_exits()
        # prev-direction: best_path[-1]
        prev_dir = best_path[-1]
        # remove prev-direction from visited[current_room.id]
        visited[player.current_room.id].remove(prev_dir)

    # while len(visited[player_current_room.id]) == 0:
    while len(visited[player.current_room.id]) == 0:
        #prev_direction = best_path.pop()
        prev_dir = best_path.pop()
        # add prev_direction to traversal_path
        traversal_path.append(prev_dir)
        # player.travel(prev_direction)
        player.travel(prev_dir)

    #next_move = visited[current_room.id].pop(0)
    next_move = visited[player.current_room.id].pop(0)
    # traversal_path.append(next_move)
    traversal_path.append(next_move)
    # best_path.append(reverse[next_move])
    best_path.append(reverse[next_move])
    # player.travel(next_move)
    player.travel(next_move)

# curr_room = s.pop()
# print(curr_room, 'current room')

# if curr_room.id not in visited:
#     # put in visited
#     room_exits = curr_room.get_exits()
#     visited[curr_room.id] = room_exits
#     print(room_exits, 'room exits')
#     # I AM NOT UPDATING THE ROOM EXIT VALUES FOR WHERE EACH EXIT POINTS
#     for room_exit in room_exits:

#         next_room = curr_room.get_room_in_direction(room_exit)
#         visited[curr_room.id] =

#         if next_room not in visited:
#             # move toward that exit
#             player.travel(room_exit)
#             # log direction in traversal path
#             traversal_path.append(room_exit)
#             new_room = player.current_room
#             print(new_room, "new room")
#             # add newest current room
#             s.push(new_room)
#             player.travel(reverse[room_exit])

# else:
#     print("you've already been here")
# q.enqueue(curr_room)

# while q.size() > 0:

#     current_room = q.dequeue()

# i am looking for a room whose value contains ?

# BFS to shortest room with '?' for an exit

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

    #######
    # UNCOMMENT TO WALK AROUND
    #######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
