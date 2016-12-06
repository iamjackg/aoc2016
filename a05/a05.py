import hashlib

counter = 0
password = ''
start = 'reyedfim'

while len(password) < 8:
    h = hashlib.md5(start + str(counter)).hexdigest()
    if h.startswith('0' * 5):
        password += h[5]
        print password
    counter += 1
