from functools import partial
from string import ascii_lowercase


size = 60  # try different sizes


with open('fear.txt') as stream:
    while True:
        data = stream.read(size)
        if data.strip():
            print('===>', data, '<===')
        else:
            break
