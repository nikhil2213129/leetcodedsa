class Solution(object):
    def prefixesDivBy5(self, nums):
        res = []
        b = 0
        for i in nums:
            b = b * 2 + i
            res.append(b % 5 == 0)
        return res
