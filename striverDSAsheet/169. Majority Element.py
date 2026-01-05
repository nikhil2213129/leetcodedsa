class Solution(object):
    def majorityElement(self, nums):
        k = len(nums)//2
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
            if hash[i] > k:
                return i
