import os
import hashlib


def adventcoin_mine(salt, zeros):
    i = 1
    md5_hash = hashlib.md5((salt+"1").encode('utf8')).hexdigest()
    while md5_hash[:zeros] != "".rjust(zeros, '0'):
        i += 1
        md5_hash = hashlib.md5((salt+str(i)).encode('utf8')).hexdigest()
    return i

with open(os.path.dirname(os.path.realpath('__file__')) + "/day4.txt", "r") as datafile:
    data = datafile.read().replace('\n', '')

print(adventcoin_mine(data, 5))
print(adventcoin_mine(data, 6))
