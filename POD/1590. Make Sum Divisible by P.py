class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        k = sum(nums) % p
        if k == 0:
            return 0

        prefix_sums = {0: -1}   # remainder -> index
        curr_sum = 0
        res = len(nums)

        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            target = (curr_sum - k) % p
            if target in prefix_sums:
                res = min(res, i - prefix_sums[target])
            prefix_sums[curr_sum] = i

        return res if res < len(nums) else -1
