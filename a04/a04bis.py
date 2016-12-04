import re

regex = re.compile('(.*?)-(\d+)\[([a-z]+)')

with open('input', 'r') as input_file:
    for line in input_file:
        match = regex.match(line)
        name, location, checksum = match.groups()

        rot = int(location)

        final = ''

        for letter in name:
            final += chr(((ord(letter) - 97 + rot) % 26) + 97)

        if 'pole' in final:
            print final, location
