from collections import defaultdict

robots = defaultdict(list)
outputs = defaultdict(int)

commands = []

with open('input.txt', 'r') as input_file:
    for line in input_file:
        data = line.split()
        if 'value' in line:
            robots[data[-1]].append(int(data[1]))
        else:
            commands.append([data[1], data[5], data[6], data[10], data[11]])


def do_command(giver, lowWho, lowID, highWho, highID):
    for who, id, func in [[lowWho, lowID, min], [highWho, highID, max]]:
        if who == 'output':
            outputs[id] += min(robots[giver])
            robots[giver].remove(min(robots[giver]))
        else:
            robots[id].append(min(robots[giver]))
            robots[giver].remove(min(robots[giver]))

while commands:
    for command in commands:
        if len(robots[command[0]]) == 2:
            do_command(*command)

            commands.remove(command)
            break

print outputs['0']*outputs['1']*outputs['2']
