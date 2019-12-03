import numpy as np
import sys

def intcode(input_dat, noun=12, verb=2):

    # copy data so don't overwrite it
    dat = np.zeros_like(input_dat)
    dat[:] = input_dat
    
    dat[1] = noun
    dat[2] = verb

    pos = 0

    while dat[pos] != 99:
        x_pos, y_pos = dat[pos+1:pos+3]
        output_pos = dat[pos+3]

        if dat[pos] == 1:
            # add 
            dat[output_pos] = dat[x_pos] + dat[y_pos]
        elif dat[pos] == 2:
            # multiply
            dat[output_pos] = dat[x_pos] * dat[y_pos]
        
        pos+= 4

    return dat[0]

def find_inputs(dat, target=19690720):

    max_val = 99

    for noun in range(max_val):
        for verb in range(max_val):
            try:
                output = intcode(dat, noun, verb)
            except IndexError:
                output = -1

            if output == target:
                return noun, verb
            

if __name__ == "__main__":

    dat = np.loadtxt(sys.argv[1], ndmin=1, delimiter=',', dtype=np.int)
    
    part1 = intcode(dat)

    print(f'Part 1, dat0 = {part1}')

    noun, verb = find_inputs(dat)

    print(f'Part 2, product = {100 * noun + verb}')


