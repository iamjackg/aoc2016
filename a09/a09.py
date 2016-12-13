state = 'read'

with open('input.txt', 'r') as input_file:
    for line in input_file:
        line = line.strip()
        final_string = ''
        while line:
            if line[0] == '(':
                end = line.find(')')
                instruction = line[1:end]
                amount, multiplier = map(int, instruction.split('x'))
                line = line[end+1:]
                segment = line[:amount]
                final_string += segment * int(multiplier)
                line = line[amount:]
            else:
                final_string += line[0]
                line = line[1:]
        print final_string
        print len(final_string)
