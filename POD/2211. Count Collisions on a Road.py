class Solution(object):
    def countCollisions(self, directions):
        directions = directions.lstrip('L').rstrip('R')
        collisions = 0
        ptr = 0
        while ptr<len(directions):
            if directions[ptr] != 'S':
                collisions += 1
            ptr+=1
        return collisions
