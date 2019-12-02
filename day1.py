import numpy as np
import sys

def fuel(input_file):
    dat = np.loadtxt(input_file, ndmin=1)

    total_fuel = int(np.sum((dat / 3) // 1 - 2))

    print(f'total fuel required = {total_fuel}')

    print(f'part 2')

    total_fuel = 0

    for mass in dat:
        intermediate_fuel = 0
        f = int((mass / 3) // 1 - 2)
        while f > 0:
            intermediate_fuel += f
            f = int((f / 3) // 1 - 2)

        total_fuel += intermediate_fuel


    print(f'total fuel required = {total_fuel}')




if __name__ == "__main__":
    
    fuel(sys.argv[1])