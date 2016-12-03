but_x = 2
but_y = 1

operations = {'L': lambda x: max(x-1, 1),
              'R': lambda x: min(x+1, 3),
              'U': lambda y: max(y-1, 0),
              'D': lambda y: min(y+1, 2)}

with open('input', 'r') as input_file:
    for line in input_file:
        for command in line.strip():
            if command in 'LR':
                but_x = operations[command](but_x)
            else:
                but_y = operations[command](but_y)
        print 'Button {0}'.format(but_x+(but_y*3))
