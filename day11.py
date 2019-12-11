import numpy as np
import sys
import cmath
import matplotlib.pyplot as plt

def int_code(input_dat, initial_panel=0):

    pos = 0

    # copy data so don't overwrite it
    dat = np.zeros_like(input_dat, dtype=np.int64)
    dat[:] = input_dat

    intcode = int(str(dat[pos])[-2:])
    modes = [int(x) for x in str(dat[pos])[:-2]][::-1]

    output = []

    relative_base = 0
    panels = {(0,0): initial_panel}
    direction = 1j
    robot_pos = (0,0)

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
                try:
                    dat[mode_pos(dat[pos+1], modes[0])] = panels[robot_pos]
                except KeyError:
                    dat[mode_pos(dat[pos+1], modes[0])] = 0
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

            if len(output) == 2:
                # found both paint colour and turning direction 

                # paint it 
                panels[robot_pos] = output[0]

                # rotate it 
                _, phi = cmath.polar(direction)
                if output[1] == 0:
                    # turn left 
                    direction = cmath.rect(1, phi + np.pi/2)
                else:
                    # turn right
                    direction = cmath.rect(1, phi - np.pi/2)

                # move forwards one step 
                robot_pos = (robot_pos[0]+round(direction.real), robot_pos[1]+round(direction.imag))

                output = []


        except IndexError:
            dat = np.pad(dat, (0, len(dat)), mode="constant")    
    
    return len(panels), panels

def print_panels(panels):
    # find corner panels 
    min_x = min(panels, key=lambda x: x[0])[0]
    min_y = min(panels, key=lambda x: x[1])[1]

    max_x = max(panels, key=lambda x: x[0])[0]
    max_y = max(panels, key=lambda x: x[1])[1]

    # now make a grid
    grid = np.zeros((max_x-min_x+1, max_y-min_y+1))

    for p, colour in panels.items():
        grid[p[0]-min_x, p[1]-min_y] = colour 

    fig, ax = plt.subplots()

    ax.imshow(np.rot90(grid))

    fig.savefig('message.png')
    

if __name__ == "__main__":

    dat = np.loadtxt(sys.argv[1], ndmin=1, delimiter=',', dtype=np.int)
    
    part1, _ = int_code(dat)

    print(f'Part 1 = {part1}')
    
    _, panels = int_code(dat, 1)

    print_panels(panels)

