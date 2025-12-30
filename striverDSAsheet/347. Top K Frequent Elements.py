class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        s = sorted(d.items(), key=lambda item : (-item[1],item[0]))
        return [word for word,freq in s[:k]]
        
