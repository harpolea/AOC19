import numpy as np
import sys
import cmath

def find_asteroids(infile):

    asteroids = set()

    for i, row in enumerate(infile.readlines()):
        for j, c in enumerate(row):
            if c == '#':
                asteroids.add((j,i))

    return asteroids

def count_asteroids(asteroids):

    max_seen = 0
    best_loc = (0,0)

    # we're going to calculate normal vectors from each asteroid to all the others. 
    # If norm is not in the set of already found norms, add one to the total seen 
    for station in asteroids:
        locs = set()
        for a in asteroids:
            if a != station:
                norm_vec = np.array([station[0] - a[0], station[1] - a[1]])
                norm_vec = norm_vec / np.linalg.norm(norm_vec)
                locs.add((np.around(norm_vec[0], decimals=4), np.around(norm_vec[1], decimals=4)))

        if len(locs) > max_seen:
            max_seen = len(locs)
            best_loc = station

    return max_seen, best_loc

def vaporise_them_all(asteroids, station):
    locs = dict()
    original_positions = dict()
    for a in asteroids:
        if a != station:
            x, y = a[0], a[1]
            z = complex(-(a[1] - station[1]) , a[0] - station[0])
            r, phi = cmath.polar(z)

            if phi < 0:
                phi = np.pi * 2 + phi

            phi = np.around(phi, decimals=4)

            original_positions[(r, phi)] = x,y

            if phi in locs:
                locs[phi].append(r)
            else:
                locs[phi] = [r]

    # sort the phis 
    for k, v in locs.items():
        locs[k] = sorted(v)

    # now let's vaporise!

    n_asteroids = 0
    r, phi = 0,0
    while n_asteroids < 200:
        new_locs = dict()
        for k in sorted(locs):
            v = locs[k]
            if len(v) > 1:
                new_locs[k] = v[1:]
            n_asteroids += 1
            r, phi = v[0], k

            if n_asteroids == 200:
                break

        locs = new_locs

    x, y = original_positions[(r,phi)]

    return 100 * x + y


if __name__ == "__main__":

    with open(sys.argv[1]) as infile:
        asteroids = find_asteroids(infile)

        max_seen, best_loc = count_asteroids(asteroids)

        print(f'Part 1 = {max_seen}, {best_loc}')

        output = vaporise_them_all(asteroids, best_loc)

        print(f'Part 2 = {output}')