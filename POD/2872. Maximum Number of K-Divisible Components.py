class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        h = defaultdict(list)
        for i, j in edges:
            h[i].append(j)
            h[j].append(i)
        r = 0

        def dfs(cur, parent):
            t = values[cur]
            for child in h[cur]:
                if child != parent:
                    t += dfs(child, cur)
            if t % k == 0:
                nonlocal r
                r += 1
                return 0
            return t

        dfs(0, -1)
        return r
