from itertools import islice


def sliding_window(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)


def is_palyndrome(string):
    return sum([string[i] == string[-i-1] for i in range(len(string) / 2)]) == len(string) / 2


def has_abba(string):
    for four_gram in sliding_window(string, 4):
        if is_palyndrome(four_gram) and four_gram[0] != four_gram[1]:
            return True

    return False

counter = 0

with open('input', 'r') as input_file:
    for line in input_file:
        pieces = line.replace(']', '[').split('[')
        normal, hypernet = [pieces[i::2] for i in range(2)]
        if True not in [has_abba(segment) for segment in hypernet] and True in [has_abba(segment) for segment in normal]:
                counter += 1

print counter
