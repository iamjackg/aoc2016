from __future__ import print_function

direction_coefficients = ((0, 1),
                          (1, 0),
                          (0, -1),
                          (-1, 0))

data = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, " \
       "L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, " \
       "L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, " \
       "R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, " \
       "L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, " \
       "L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, " \
       "L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, " \
       "R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"

current_direction = 0

current_position = [0, 0]

places_and_stuff = set()

for command in data.split(', '):
    if command[0] == 'L':
        current_direction = (current_direction - 1) % 4
    elif command[0] == 'R':
        current_direction = (current_direction + 1) % 4
    else:
        print("We're not playing the same game, you and I.")
        exit(1)

    multiplier = int(command[1:])

    for steppy_step in range(multiplier):
        current_position = [current_position[0] + direction_coefficients[current_direction][0],
                            current_position[1] + direction_coefficients[current_direction][1]]

        if tuple(current_position) in places_and_stuff:
            print("What? You've been here before!\nYou're at x: {1}, y: {2}\nYour distance from the start is {0}.""".format(sum([abs(coordinate) for coordinate in current_position]), *current_position))
            exit(0)

        places_and_stuff.add(tuple(current_position))
