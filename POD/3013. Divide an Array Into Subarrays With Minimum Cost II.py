class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        minCostSum = float("inf")
        maxHeap = []
        minRightSum = 0
        indices = set()
        minHeap = []
        
        for i in range(2, min(dist + 2, n)):
            heappush(maxHeap, [-nums[i], -i, i])
            minRightSum += nums[i]
            indices.add(i)

            if len(indices) > k - 2:
                val, _, idx = heappop(maxHeap)
                heappush(minHeap, [-val, idx, idx])
                minRightSum -= -val
                indices.remove(idx)
                    
        for i in range(1, n - (k - 2)):
            while maxHeap and maxHeap[0][2] not in indices: 
                heappop(maxHeap)
            while minHeap and minHeap[0][2] <= i: 
                heappop(minHeap)
                    
            minCostSum = min(minCostSum, nums[0] + nums[i] + minRightSum)
                
            if i + 1 in indices:
                minRightSum -= nums[i + 1]
                indices.remove(i + 1)
                if minHeap: 
                    top = heappop(minHeap)
                    heappush(maxHeap, [-top[0], -top[2], top[2]])
                    indices.add(top[2])
                    minRightSum += top[0]

            if i + 1 + dist < n:
                heappush(maxHeap, [-nums[i + 1 + dist], -(i + 1 + dist), i + 1 + dist])
                minRightSum += nums[i + 1 + dist]
                indices.add(i + 1 + dist)

                if len(indices) > k - 2:
                    val, _, idx = heappop(maxHeap)
                    heappush(minHeap, [-val, idx, idx])
                    minRightSum -= -val
                    if idx in indices: 
                        indices.remove(idx)

        return minCostSum
