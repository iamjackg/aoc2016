counter = 0
group = []

with open('input', 'r') as input_file:
    for line in input_file:
        sides = [int(field) for field in line.split()]
        group.append(sides)
        counter += 1
        if len(group) == 3:
            for possible_triangle in zip(*group):
                for index in range(-3, 0):
                    if (possible_triangle[index] + possible_triangle[index+1]) <= possible_triangle[index+2]:
                        counter -= 1
                        break
            group = []

print "{0} triangles".format(counter)
