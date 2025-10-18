class Solution(object):
    def maxDistinctElements(self, nums, k):
        n = len(nums)
        snums = sorted(nums)
        y= len(set(snums))
        
        if k >= n:
            return n
        if y==n:
            return n  
        if 2*k >= n-y:
            return n
        seen = set()
        next_free = {}

        def find(x):
            if x in next_free:
                next_free[x] = find(next_free[x]) 
                return next_free[x]
            return x

        for num in snums:
            pos = find(num - k)
            if pos <= num + k: 
                seen.add(pos)
                next_free[pos] = pos + 1 
        return len(seen)
