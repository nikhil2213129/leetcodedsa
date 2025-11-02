class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        visited = set()
        guards_set = set(map(tuple, guards))
        walls_set = set(map(tuple, walls))

        for i in guards:
            visited.add(tuple(i))
        for j in walls:
            visited.add(tuple(j))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if (i, j) in guards_set:
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        while 0 <= x < m and 0 <= y < n:
                            if (x, y) in guards_set or (x, y) in walls_set:
                                break
                            visited.add((x, y))
                            x += dx
                            y += dy

        return m * n - len(visited)
