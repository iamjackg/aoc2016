pos = [-2, 0]

absum = lambda array: sum([abs(i) for i in array])

labels = {}
start = 1
for y in range(-2, 3):
    for x in range(-2, 3):
        if absum([x, y]) <= 2:
            labels[(x, y)] = hex(start)[2:]
            start += 1

operations = {'L': lambda c: [max(c[0]-1, -2), c[1]] if not (c[0] <  1 and absum(c) == 2) else c,
              'R': lambda c: [min(c[0]+1,  2), c[1]] if not (c[0] > -1 and absum(c) == 2) else c,
              'U': lambda c: [c[0], max(c[1]-1, -2)] if not (c[1] <  1 and absum(c) == 2) else c,
              'D': lambda c: [c[0], min(c[1]+1,  2)] if not (c[1] > -1 and absum(c) == 2) else c}

with open('input', 'r') as input_file:
    for line in input_file:
        for command in line.strip():
            pos = operations[command](pos)
        print 'Button {0}'.format(labels[tuple(pos)])
