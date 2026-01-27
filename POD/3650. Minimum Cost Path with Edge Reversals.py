import heapq
from collections import defaultdict
# from typing import List
class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, 2 * wt))  # reversed edge

        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, node = heapq.heappop(pq)
            if node == n - 1:
                return d
            if d > dist[node]:
                continue
            for adjNode, weight in adj[node]:
                if d + weight < dist[adjNode]:
                    dist[adjNode] = d + weight
                    heapq.heappush(pq, (dist[adjNode], adjNode))

        return -1
        
