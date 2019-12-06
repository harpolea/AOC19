import numpy as np
import sys

def count_orbits(input_file):

    orbits = {'COM': None}
    satellites = set()

    # read file and make a dictionary of orbits 
    with open(input_file, 'r') as infile:
        for line in infile:
            inner, outer = line.replace('\n', '').split(')')

            orbits[outer] = inner 
            satellites.add(outer)
            satellites.add(inner)
    
    # loop over satellites to count orbits 
    counter = 0
    for s in satellites:
        outer = s
        inner = orbits[outer]
        while inner is not None:
            counter += 1
            outer = inner
            inner = orbits[outer]

    print(f'There are {counter} orbits')

    return orbits

def orbit_transfers(orbits):
    # to do this shall find orbits from YOU, SAN to COM, then count lengths of 
    # paths to first common satellite

    YOU_path = []
    outer = 'YOU'
    inner = orbits[outer]
    while inner is not None:
        YOU_path.append(inner)
        outer = inner 
        inner = orbits[outer]

    SAN_path = []
    outer = 'SAN'
    inner = orbits[outer]
    while inner is not None:
        SAN_path.append(inner)
        outer = inner 
        inner = orbits[outer]

    # now find first common satellite 
    for i, s in enumerate(YOU_path):
        try:
            print(f'{i + SAN_path.index(s)} transfers are needed')
            break
        except ValueError:
            continue



if __name__ == "__main__":

    orbits = count_orbits(sys.argv[1])

    orbit_transfers(orbits)