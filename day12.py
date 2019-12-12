import numpy as np
import sys
import re

DIM = 3

class Moon(object):

    def __init__(self, pos):
        self.pos = np.array(pos)
        self.vel = np.zeros_like(self.pos)

    def apply_gravity(self, planets):
        for p in planets:
            self.vel += np.sign(p.pos - self.pos)

    def apply_velocity(self):
        self.pos += self.vel

    def calc_energy(self):
        # potential energy 
        V = np.sum(np.abs(self.pos))
        # kinetic energy
        K = np.sum(np.abs(self.vel))

        return V * K

def find_moons(infile):

    r = re.compile(r'(-?\d+),\s*y=(-?\d+),\s*z=(-?\d+)')

    moons = []

    for l in infile.readlines():
        m = r.search(l)
        pos = [int(x) for x in m.groups()]
        moons.append(Moon(pos))

    return moons

def simulate_moons(moons, n_steps):

    for n in range(n_steps):
        for m in moons:
            m.apply_gravity(moons)
        
        for m in moons:
            m.apply_velocity()

    # finally find total energy 
    return sum([m.calc_energy() for m in moons])


def find_periods(moons):
    ps = np.zeros(DIM, dtype=np.int)

    for i in range(DIM):
        xs = np.array([m.pos[i] for m in moons])
        initial_xs = np.zeros_like(xs) + xs
        vs = np.zeros_like(xs)

        # iterate until xs == initial_xs
        while True:
            # apply grav 
            for j in range(len(moons)):
                vs[j] += sum(np.sign(xs - xs[j]))
            
            # apply vel 
            xs += vs 

            ps[i] += 1

            if np.all(xs == initial_xs):
                break


    return np.lcm.reduce(ps+1)

if __name__ == "__main__":

    with open(sys.argv[1]) as infile:
        moons = find_moons(infile)

    TE = simulate_moons(moons, int(sys.argv[2]))

    print(f'Total energy = {TE}')

    # reset 
    with open(sys.argv[1]) as infile:
        moons = find_moons(infile)

    part2 = find_periods(moons)

    print(f'Number of steps = {part2}')