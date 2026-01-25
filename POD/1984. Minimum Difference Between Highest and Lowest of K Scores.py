class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums.sort()
        max_diff = nums[k-1]-nums[0]
        for i in range(k-1,len(nums)):
            diff = nums[i] - nums[i-(k-1)]
            max_diff = min(max_diff,diff)
        return max_diff

        
