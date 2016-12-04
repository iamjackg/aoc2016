from collections import Counter
import re
import itertools

total_sum = 0

regex = re.compile('(.*?)-(\d+)\[([a-z]+)')

with open('input', 'r') as input_file:
    for line in input_file:
        match = regex.match(line)
        name, location, checksum = match.groups()

        c = Counter(name)
        del c['-']

        # This gives us all the characters in descending order of occurrences.
        # Unfortunately ties are _not_ solved alphabetically, so we'll have to do some more magic.
        top_characters = c.most_common()

        correctly_ordered = []

        # We sort each group of same-amount characters in alphabetical order
        for stuff in itertools.groupby(top_characters, lambda couple: couple[1]):
            map(correctly_ordered.append, sorted(stuff[1], key=lambda couple: couple[0]))

        # The correct checksum is made of the top 5 characters
        correct_checksum = ''.join([couple[0] for couple in correctly_ordered][:5])

        if checksum == correct_checksum:
            total_sum += int(location)

print total_sum
