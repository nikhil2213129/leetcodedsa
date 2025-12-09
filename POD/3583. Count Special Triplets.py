class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        MOD = 10**9 + 7
        left = Counter()
        right = Counter(nums)
        result = 0
        
        for num in nums:
            right[num] -= 1
            target = num * 2
            result = (result + left[target] * right[target]) % MOD
            left[num] += 1
        
        return result
