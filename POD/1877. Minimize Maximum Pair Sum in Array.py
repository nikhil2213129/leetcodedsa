class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ptr1 = 0
        ptr2 = len(nums)-2
        max_pair_sum = nums[0]+nums[1]
        while ptr1<ptr2:
            nums[ptr1],nums[ptr2] = nums[ptr2],nums[ptr1]
            max_pair_sum = max(max_pair_sum, nums[ptr1]+nums[ptr1+1],nums[ptr2]+nums[ptr2+1])
            ptr1+=1
            ptr2-=1
        return max_pair_sum
