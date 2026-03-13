class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        h = mountainHeight
        wt = workerTimes
        res, pq = 0, sorted(map(lambda x: (x, x, 1), wt))
        while h:
            res, step, m = heappop(pq)
            h -= 1
            heappush(pq, (res + (m + 1) * step, step, m + 1))
        return res        
        
