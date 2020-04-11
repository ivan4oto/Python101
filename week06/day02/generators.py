import zipfile
from os import listdir
from os.path import isfile, join

def chain(one, two):
    for x in one:
        yield x
    for y in two:
        yield y

def compress(iterable, mask):
    for i in range(len(mask)):
        if mask[i]:
            yield iterable[i]

def cycle(iterable):
    i = 0
    while True:
        if i > len(iterable)-1:
            i = 0 
        yield iterable[i]
        i += 1

