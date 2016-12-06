from collections import Counter

print ''.join([Counter(column).most_common(1)[0][0] for column in zip(*open('input.txt', 'r').readlines())])
