import numpy as np
import sys

def find_intersection(input_file):
    with open(input_file, 'r') as infile:
        w1, w2 = infile.readlines()

        w1 = w1.replace('\n', '')
        w1 = w1.split(',')
        w2 = w2.split(',')

        # map of directions
        dir = {'R': (1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}

        # first we're going to store the first wire's path in a set
        path = set()
        pos = np.array([0,0])

        for move in w1:
            new_pos = pos + np.array(dir[move[0]]) * int(move[1:])

            for x in range(min(pos[0], new_pos[0]), 
                           max(pos[0], new_pos[0])+1):
                for y in range(min(pos[1], new_pos[1]), 
                               max(pos[1], new_pos[1])+1):
                    path.add((x,y))

            pos = new_pos

        path.add((x,y))

        # now we're going to follow the second wire and store nearest intersection point found 
        closest_distance = 100000
        pos = np.array([0,0])

        for move in w2:
            new_pos = pos + np.array(dir[move[0]]) * int(move[1:])
            for x in range(min(pos[0], new_pos[0]), 
                           max(pos[0], new_pos[0])+1):
                for y in range(min(pos[1], new_pos[1]), 
                               max(pos[1], new_pos[1])+1):
                    if (x,y) in path and (x != 0 and y != 0):
                        distance = abs(x) + abs(y)
                        closest_distance = min(distance, closest_distance)

            pos = new_pos

        x, y = pos
        if (x,y) in path and x != 0 and y != 0:
            distance = abs(x) + abs(y)
            closest_distance = min(distance, closest_distance)

        print(f'closest intersection = {closest_distance}')

        return closest_distance

def find_minimal_delay_intersect(input_file):
    with open(input_file, 'r') as infile:
        w1, w2 = infile.readlines()

        w1 = w1.replace('\n', '')
        w1 = w1.split(',')
        w2 = w2.split(',')

        # map of directions
        dir = {'R': (1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}

        # first we're going to store the first wire's path in a set
        path = {}
        pos = np.array([0,0])
        steps = 0

        for move in w1:
            new_pos = pos + np.array(dir[move[0]]) * int(move[1:]) 
            
            if move[0] == 'R':
                for x in range(pos[0]+1, new_pos[0]+1):
                    steps += 1
                    path.setdefault((x,pos[1]), steps)
            elif move[0] == 'L':
                for x in range(pos[0]-1, new_pos[0]-1, -1):
                    steps += 1
                    path.setdefault((x,pos[1]), steps)
            elif move[0] == 'U':
                for y in range(pos[1]+1,new_pos[1]+1):
                    steps += 1
                    path.setdefault((pos[0], y), steps)
            else:
                for y in range(pos[1]-1,new_pos[1]-1,-1):
                    steps += 1
                    path.setdefault((pos[0], y), steps)


            pos = new_pos

        # now we're going to follow the second wire and store nearest intersection point found 
        min_steps = 100000
        pos = np.array([0,0])
        steps = 0

        for move in w2:
            new_pos = pos + np.array(dir[move[0]]) * int(move[1:])
            
            if move[0] == 'R':

                for x in range(pos[0]+1, new_pos[0]+1):
                    steps += 1
                    if x != 0 and pos[1] != 0 and (x,pos[1]) in path:
                        print((x,pos[1]), path[(x,pos[1])], steps)
                        min_steps = min(path[(x,pos[1])] + steps, min_steps)
            elif move[0] == 'L':
                for x in range(pos[0]-1, new_pos[0]-1, -1):
                    steps += 1
                    if x != 0 and pos[1] != 0 and (x,pos[1]) in path:
                        print((x,pos[1]), path[(x,pos[1])], steps)
                        min_steps = min(path[(x,pos[1])] + steps, min_steps)

            elif move[0] == 'U':
                for y in range(pos[1]+1,new_pos[1]+1):
                    steps += 1
                    if pos[0] != 0 and y != 0 and (pos[0],y) in path:
                        print((pos[0],y), path[(pos[0],y)], steps)
                        min_steps = min(path[(pos[0],y)] + steps, min_steps)

            else:
                for y in range(pos[1]-1,new_pos[1]-1,-1):
                    steps += 1
                    if pos[0] != 0 and y != 0 and (pos[0],y) in path:
                        print((pos[0],y), path[(pos[0],y)], steps)
                        min_steps = min(path[(pos[0],y)] + steps, min_steps)
            pos = new_pos

        print(f'fewest combined steps = {min_steps}')

        return min_steps
            
                    
        
if __name__ == "__main__":

    # find_intersection(sys.argv[1])
    find_minimal_delay_intersect(sys.argv[1])


