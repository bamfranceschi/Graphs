from util import Queue

# Build our graph
# could filter our word list by length
# remember to lower case stuff
# BFS

# for every letter in the word,
# swap out a letter in the alphabet
# if the result is in our words list, it's a neighbor

word_list = set()
for word in words:
    word_list.add(word.lower())


def get_neighbors(start_word):
    neighbors = []
    for word_letter in word:
    for letter_index in range(len(start_word)):
        for letter in string.ascii_lowercase:
            # not going to work, strings are immutable. turn the word into a list then sub out the letter. then turn it back into a string
            # make sure everyting is lowercase too
            word_list = list(start_word)
            word_list[letter_index] = letter

            word = "".join(word_list)

            if word in word_list and word != start_word:
                neighbors.append(word)

    return neighbors


def word_letters(start_word, end_word):
    q = Queue()

    visited = set()

    q.enqueue([start_word])

    while q.size():

        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visited:
            visited.add(current_word)

        neighbors = get_neighbors(current_word)

        for neighbor in neighbors:
            q.enqueue(current_path + [neighbor])
