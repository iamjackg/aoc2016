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
            outputs[id] += func(robots[giver])
            robots[giver].remove(func(robots[giver]))
        else:
            robots[id].append(func(robots[giver]))
            robots[giver].remove(func(robots[giver]))

while commands:
    for command in commands:
        if len(robots[command[0]]) == 2:
            if 61 in robots[command[0]] and 17 in robots[command[0]]:
                print 'Robot', command[0]
                exit()
            do_command(*command)

            commands.remove(command)
            break
