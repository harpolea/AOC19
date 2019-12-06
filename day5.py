import numpy as np
import sys

def int_code(input_dat):

    # copy data so don't overwrite it
    dat = np.zeros_like(input_dat)
    dat[:] = input_dat

    pos = 0

    output = []

    intcode = int(str(dat[pos])[-2:])
    modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

    def val(param, mode=0):
        if mode == 0:
            return dat[param]
        else:
            return param

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
            dat[dat[pos+1]] = int(input('Input a value: '))
            pos+= 2
        elif intcode == 4:
            # pad modes 
            modes += [0] * (1 - len(modes))
            output.append(val(dat[pos+1], modes[0]))
            pos += 2

        intcode = int(str(dat[pos])[-2:])
        modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

    return output

def int_code2(input_dat):

    # copy data so don't overwrite it
    dat = np.zeros_like(input_dat)
    dat[:] = input_dat

    pos = 0

    output = []

    intcode = int(str(dat[pos])[-2:])
    modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

    def val(param, mode=0):
        if mode == 0:
            return dat[param]
        else:
            return param

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
            dat[dat[pos+1]] = int(input('Input a value: '))
            pos+= 2
        elif intcode == 4:
            # pad modes 
            modes += [0] * (1 - len(modes))
            output.append(val(dat[pos+1], modes[0]))
            pos += 2
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

    return output

            

if __name__ == "__main__":

    dat = np.loadtxt(sys.argv[1], ndmin=1, delimiter=',', dtype=np.int)
    
    part1 = int_code(dat)

    print(f'Part 1 = {part1[-1]}')
    
    part2 = int_code2(dat)

    print(f'Part 2 = {part2[-1]}')

