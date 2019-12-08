import numpy as np
import sys

def layers(dat, w=25, h=6):

    image_size = w * h

    # break list into layers 
    layer_dat = [dat[n*image_size:n*image_size+image_size] for n in range(len(dat) // image_size)]

    fewest_zeros = image_size

    output = 1

    for layer in layer_dat:
        if layer.count('0') < fewest_zeros:
            output = layer.count('1') * layer.count('2')
            fewest_zeros = layer.count('0')

    return output

def decode(dat, w=25, h=6):

    image_size = w * h

    # break list into layers 
    layer_dat = [dat[n*image_size:n*image_size+image_size] for n in range(len(dat) // image_size)]

    # now want to transpose this so can access pixels 
    output = [''.join([row[i] for row in layer_dat]).replace('2', '')[0] for i in range(len(layer_dat[0]))]

    for i in range(h):
        row = ''
        for j in range(w):
            row += ' ' if output[i*w + j]=='0' else 'x'
        print(row)


if __name__ == "__main__":

    with open(sys.argv[1]) as infile:
        output = layers(infile.read())

        print(f'Part 1 = {output}')

    with open(sys.argv[1]) as infile:
        decode(infile.read())