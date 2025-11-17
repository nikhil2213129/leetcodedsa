class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1 and count == 0:
                count = 1
                prev = i
            elif nums[i] == 1 and count == 1:
                x = i-prev-1
                prev = i
                if x >= k:
                    continue 
                else:
                    return False
        return True
                
                    
                
