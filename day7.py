import numpy as np
import sys
from itertools import permutations

def int_code(input_dat, input_vals, pos=0):

    # copy data so don't overwrite it
    dat = np.zeros_like(input_dat)
    dat[:] = input_dat

    intcode = int(str(dat[pos])[-2:])
    modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

    def val(param, mode=0):
        if mode == 0:
            return dat[param]
        else:
            return param

    first_input = True

    while intcode != 99:

        if intcode == 1:
            # pad modes 
            modes += [0] * (2 - len(modes))
            # add 
            dat[dat[pos+3]] = val(dat[pos+1], modes[0]) + val(dat[pos+2], modes[1])
            pos+= 4
        elif intcode == 2:
            # pad modes 
            modes += [0] * (2 - len(modes))
            # multiply
            dat[dat[pos+3]] = val(dat[pos+1], modes[0]) * val(dat[pos+2], modes[1])
            pos+= 4
        elif intcode == 3:
            # pad modes 
            dat[dat[pos+1]] = input_vals[0] if first_input else input_vals[1]
            first_input = False
            pos+= 2
        elif intcode == 4:
            # pad modes 
            modes += [0] * (1 - len(modes))
            return val(dat[pos+1], modes[0]), pos+2, dat
        elif intcode == 5:
            # pad modes 
            modes += [0] * (2 - len(modes))
            if val(dat[pos+1], modes[0]) != 0:
                pos = val(dat[pos+2], modes[1])
            else:
                pos += 3
        elif intcode == 6:
            # pad modes 
            modes += [0] * (2 - len(modes))
            if val(dat[pos+1], modes[0]) == 0:
                pos = val(dat[pos+2], modes[1])
            else:
                pos += 3
        elif intcode == 7:
            # pad modes 
            modes += [0] * (2 - len(modes))
            if val(dat[pos+1], modes[0]) < val(dat[pos+2], modes[1]):
                dat[dat[pos+3]] = 1
            else:
                dat[dat[pos+3]] = 0
            pos += 4
        elif intcode == 8:
            # pad modes 
            modes += [0] * (2 - len(modes))
            if val(dat[pos+1], modes[0]) == val(dat[pos+2], modes[1]):
                dat[dat[pos+3]] = 1
            else:
                dat[dat[pos+3]] = 0
            pos += 4

        intcode = int(str(dat[pos])[-2:])
        modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

    return None

def find_signal(dat):

    max_signal = 0

    for amps in list(permutations(range(5))):

        output = 0

        for amp in amps:
            output,_,_ = int_code(dat, [amp, output])

        max_signal = max(max_signal, output)

    return max_signal

def feedback(dat):

    max_signal = 0

    for amp_phases in list(permutations(range(5,10))):

        amps = {p: (0, dat) for p in amp_phases}

        output = 0

        out_signal = 0

        for amp, (pos, data) in amps.items():
            try:
                out_signal, new_dat, new_pos = int_code(data, [amp, output], pos)
                output = out_signal
                amps[amp] = (new_dat, new_pos)
            except TypeError:
                out_signal = None
                break

        while out_signal is not None:
            for amp, (pos, data) in amps.items():
                try:
                    out_signal, new_dat, new_pos = int_code(data, [output], pos)
                    output = out_signal
                    amps[amp] = (new_dat, new_pos)
                except TypeError:
                    out_signal = None
                    break
        
        max_signal = max(max_signal, output)

    return max_signal
       

if __name__ == "__main__":

    dat = np.loadtxt(sys.argv[1], ndmin=1, delimiter=',', dtype=np.int)
    
    part1 = find_signal(dat)

    print(f'Part 1 = {part1}')
    
    part2 = feedback(dat)

    print(f'Part 2 = {part2}')

