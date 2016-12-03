counter = 0

with open('input', 'r') as input_file:
    for line in input_file:
        sides = [int(field) for field in line.split()]
        counter += 1
        for index in range(-3, 0):
            if (sides[index] + sides[index+1]) <= sides[index+2]:
                counter -= 1
                break

print "{0} triangles".format(counter)
