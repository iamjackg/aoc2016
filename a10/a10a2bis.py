from collections import defaultdict

robots = defaultdict(list)
outputs = defaultdict(int)

with open('input.txt', 'r') as input_file:
    for line in input_file:
        data = line.split()
        if 'value' in line:
            robots[data[-1]].append(int(data[1]))

print robots


commands = []


with open('input.txt', 'r') as input_file:
    for line in input_file:
        data = line.split()
        if 'gives' in line:
            commands.append([data[1], data[5], data[6], data[10], data[11]])

while commands:
    for command in commands:
        if len(robots[command[0]]) == 2:
            if command[1] == 'output':
                outputs[command[2]] += min(robots[command[0]])
                robots[command[0]].remove(min(robots[command[0]]))
            else:
                robots[command[2]].append(min(robots[command[0]]))
                robots[command[0]].remove(min(robots[command[0]]))

            if command[3] == 'output':
                outputs[command[4]] += max(robots[command[0]])
                robots[command[0]].remove(max(robots[command[0]]))
            else:
                robots[command[4]].append(max(robots[command[0]]))
                robots[command[0]].remove(max(robots[command[0]]))

            commands.remove(command)
            break

print outputs['0']*outputs['1']*outputs['2']
