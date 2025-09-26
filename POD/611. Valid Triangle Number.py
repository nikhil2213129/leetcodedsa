from bisect import bisect_left

class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                twosidessum = nums[i]+nums[j]
                insertionpoint = bisect_left(nums,twosidessum,lo=j+1)
                largeindex = insertionpoint - 1
                count = count + (largeindex - j)
        return count 
        
