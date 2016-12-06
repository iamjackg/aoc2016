import hashlib

counter = 0
password = ['-1' for i in range(8)]
start = 'reyedfim'

while '-1' in password:
    h = hashlib.md5(start + str(counter)).hexdigest()
    if h.startswith('0' * 5) and int(h[5], 16) < 8 and password[int(h[5], 16)] == '-1':
        password[int(h[5])] = h[6]
        print password
    counter += 1

print ''.join(password)
