class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        n = len(nums)//2
        from collections import Counter
        d = Counter(nums)
        for i in d:
            if d[i] == n:
                return i

        """
        n = len(nums)/2
        for i in nums:
            if nums.count(i) == n:
                return i
        
        
