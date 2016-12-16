import sys
import time
import math

magic_number = 1358

def is_wall(x,y):
    return sum(map(int, bin(x*x + 3*x + 2*x*y + y + y*y + magic_number)[2:])) % 2 != 0

start = [1, 1]

dirs = [[0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]]

all_places = set()


def print_maze(position):
    for y in range(50):
        print ''.join(['#' if is_wall(x, y) else 'O' if [x, y] == position else '.' if tuple([x,y]) in all_places else ' ' for x in range(50)])


def go_deeper(position, visited=[], length=0):
    if -1 in position or length > 50:
        return

    new_visited = visited[:]
    new_visited.append(position)
    all_places.add(tuple(position))

    # Uncomment these for some pretty viz
    # sys.stdout.write('\033[0;0H')
    # print_maze(position)
    # print length, len(all_places)

    for direction in dirs:
        next_position = map(sum, zip(position, direction))
        if not is_wall(*next_position) and next_position not in new_visited:
            go_deeper(next_position, new_visited, length + 1)


go_deeper(start)

print len(all_places)
