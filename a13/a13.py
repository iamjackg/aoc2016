import sys
import math

magic_number = 1358

start = [1, 1]
dest = [31, 39]

dirs = [[0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]]


def is_wall(x,y):
    return sum(map(int, bin(x*x + 3*x + 2*x*y + y + y*y + magic_number)[2:])) % 2 != 0


def distance(pos1):
    return math.sqrt(sum(map(lambda n: n**2, [pos1[0] - dest[0], pos1[1] - dest[1]])))


def print_maze(position, seen):
    for y in range(50):
        print ''.join(['#' if is_wall(x, y) else 'O' if [x, y] == position else 'X' if [x, y] == dest else '.' if [x, y] in seen else ' ' for x in range(50)])

all_distances = set()


def go_deeper(position, visited=[], length=0):
    new_visited = visited[:]
    new_visited.append(position)

    if position == dest:
        all_distances.add(length)
    if -1 in position or length > 100:
        return

    sorted_dirs = sorted(dirs, key=lambda wanted_direction: distance(map(sum, zip(position, wanted_direction))))

    # Uncomment these for some pretty viz
    # sys.stdout.write('\033[0;0H')
    # print_maze(position, new_visited)
    # print length, min(all_distances) if all_distances else 0

    for direction in sorted_dirs:
        next_position = map(sum, zip(position, direction))
        if not is_wall(*next_position) and next_position not in new_visited:
            go_deeper(next_position, new_visited, length + 1)

go_deeper(start)

print min(all_distances)
