from itertools import cycle

width = 50
height = 6

screen = [list(' ' * width) for s_h in range(height)]


def rect(w, h):
    for y in range(h):
        for x in range(w):
            screen[y][x] = '#'


def rot_row(row, amount):
    for i in range(amount):
        item = screen[row].pop()
        screen[row] = [item] + screen[row]


def rot_column(column, amount):
    column_data = list(zip(*screen)[column])

    for a in range(amount):
        item = column_data.pop()
        column_data = [item] + column_data

    for i in range(height):
        screen[i][column] = column_data[i]


with open('input', 'r') as input_file:
    for line in input_file:
        words = line.split()

        if words[0][1] == 'e':
            w, h = map(int, words[1].split('x'))
            rect(w, h)
        else:
            if words[1] == 'row':
                r = int(words[2].split('=')[1])
                amount = int(words[4])
                rot_row(r, amount)
            else:
                r = int(words[2].split('=')[1])
                amount = int(words[4])
                rot_column(r, amount)


counter = 0
for line in screen:
    print ''.join(line)
    for i in line:
        if i == '#':
            counter += 1

print counter
