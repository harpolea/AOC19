import numpy as np
import sys

def find_passwords(min_input, max_input):
    count = 0

    for i in range(min_input, max_input+1):
        digits = [int(x) for x in str(i)]

        found_adjacent = False
        
        # check if there are adjacent digits that are the same 
        for a, b in zip(digits[:-1], digits[1:]):
            if a == b:
                found_adjacent = True 
                break 

        if not found_adjacent:
            continue

        # check if they never decrease 
        always_decrease = True
        for a, b in zip(digits[:-1], digits[1:]):
            if b - a < 0:
                always_decrease = False 
                break 
        
        if always_decrease:
            count += 1
    
    print(f'Found {count} passwords')

    return count

def find_passwords2(min_input, max_input):
    count = 0

    for i in range(min_input, max_input+1):
        digits = [int(x) for x in str(i)]

        found_adjacent = False
        
        # check if there are adjacent digits that are the same 
        counter = 0
        while counter < len(digits):
            n_copies = 1
            try:
                while digits[counter] == digits[counter+n_copies]:
                    n_copies += 1
            except IndexError:
                pass

            if n_copies == 2:
                found_adjacent = True 

            counter += n_copies

        if not found_adjacent:
            continue

        # check if they never decrease 
        always_decrease = True
        for a, b in zip(digits[:-1], digits[1:]):
            if b - a < 0:
                always_decrease = False 
                break 
        
        if always_decrease:
            count += 1
    
    print(f'Found {count} passwords')

    return count

            

if __name__ == "__main__":
    
    min_input, max_input = int(sys.argv[1]), int(sys.argv[2])

    find_passwords(min_input, max_input)

    print('Part 2')

    find_passwords2(min_input, max_input)