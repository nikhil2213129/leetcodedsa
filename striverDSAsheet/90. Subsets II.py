class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        nums.sort()
        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])
                return 
            subset.append(nums[i])
            create_subset(i+1)
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i + 1
            create_subset(i+1)
        create_subset(0)
        return res
