def parse_and_strip(group):
    end = group.find(')')
    amount, multiplier = map(int, group[1:end].split('x'))
    piece = group[end+1:int(amount)+end+1]

    return multiplier, piece


def group_length(group):
    if '(' in group:
        multiplier, piece = parse_and_strip(group)
        return (int(multiplier) - 1) * process(piece)
    else:
        return process(group)


def process(line):
    final_string = 0
    while line:
        if line[0] == '(':
            final_string += group_length(line)
            line = line[line.find(')') + 1:]
            print line
        else:
            final_string += 1
            line = line[1:]
    return final_string


with open('input.txt', 'r') as input_file:
    #for line in input_file:
    for line in ['(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN']:
        print process(line.strip())#print final_string
