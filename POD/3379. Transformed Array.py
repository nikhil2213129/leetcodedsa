class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0]*n
        for i in range(n):
            if nums[i]>0:
                curr = (i+nums[i])%n
                res[i] = nums[curr]
            elif nums[i]<0:
                curr = (i+nums[i])%n
                res[i] = nums[curr]
        return res
