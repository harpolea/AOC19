import numpy as np
import sys
from itertools import permutations

def int_code(input_dat, input_val=None, pos=0):

    # copy data so don't overwrite it
    dat = np.zeros_like(input_dat, dtype=np.int64)
    dat[:] = input_dat
    # dat = np.pad(dat, (0, len(dat)*10), mode="constant") 

    intcode = int(str(dat[pos])[-2:])
    modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

    output = []

    relative_base = 0

    def val(param, mode=0):
        if mode == 0:
            return dat[param]
        elif mode == 1:
            return param
        elif mode == 2:
            return dat[param + relative_base]

    def mode_pos(param, mode=0):
        if mode == 0:
            return param
        elif mode == 2:
            return param + relative_base

    while intcode != 99:

        if pos < 0:
            print('negative position!!')
            return

        try:

            if intcode == 1:
                # pad modes 
                modes += [0] * (3 - len(modes))
                if modes[-1] == 1:
                    modes[-1] = 0
                # add 
                dat[mode_pos(dat[pos+3], modes[2])] = val(dat[pos+1], modes[0]) + val(dat[pos+2], modes[1])
                pos+= 4
            elif intcode == 2:
                # pad modes 
                modes += [0] * (3 - len(modes))
                if modes[-1] == 1:
                    modes[-1] = 0
                # multiply
                dat[mode_pos(dat[pos+3], modes[2])] = val(dat[pos+1], modes[0]) * val(dat[pos+2], modes[1])
                pos+= 4
            elif intcode == 3:
                # pad modes 
                modes += [0] * (1 - len(modes))
                if modes[-1] == 1:
                    modes[-1] = 0
                dat[mode_pos(dat[pos+1], modes[0])] = input_val
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
                modes += [0] * (3 - len(modes))
                if modes[-1] == 1:
                    modes[-1] = 0
                if val(dat[pos+1], modes[0]) < val(dat[pos+2], modes[1]):
                    dat[mode_pos(dat[pos+3], modes[2])] = 1
                else:
                    dat[mode_pos(dat[pos+3], modes[2])] = 0
                pos += 4
            elif intcode == 8:
                # pad modes 
                modes += [0] * (3 - len(modes))
                if modes[-1] == 1:
                    modes[-1] = 0
                if val(dat[pos+1], modes[0]) == val(dat[pos+2], modes[1]):
                    dat[mode_pos(dat[pos+3], modes[2])] = 1
                else:
                    dat[mode_pos(dat[pos+3], modes[2])] = 0
                pos += 4
            elif intcode == 9:
                # pad modes 
                modes += [0] * (1 - len(modes))
                relative_base += val(dat[pos+1], modes[0])
                pos += 2
            else:
                return output

            intcode = int(str(dat[pos])[-2:])
            modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

        except IndexError:
            dat = np.pad(dat, (0, len(dat)), mode="constant")        

    return output
       

if __name__ == "__main__":

    dat = np.loadtxt(sys.argv[1], ndmin=1, delimiter=',', dtype=np.int)
    
    part1 = int_code(dat, 1)

    print(f'Part 1 = {part1}')
    
    part2 = int_code(dat, 2)

    print(f'Part 2 = {part2}')

