from itertools import islice, chain


def sliding_window(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)


def is_palyndrome(string):
    return sum([string[i] == string[-i-1] for i in range(len(string) / 2)]) == len(string) / 2


def get_abas(string):
    return [''.join(aba) for aba in sliding_window(string, 3) if is_palyndrome(aba) and aba[0] != aba[1]]


def aba_to_bab(aba):
    return ''.join([aba[1], aba[0], aba[1]])

counter = 0

with open('input', 'r') as input_file:
    for line in input_file:
        pieces = line.replace(']', '[').split('[')
        normal, hypernet = [pieces[i::2] for i in range(2)]
        for aba in chain(*map(get_abas, normal)):
            if aba in map(aba_to_bab, chain(*map(get_abas, hypernet))):
                counter += 1
                break

print counter
