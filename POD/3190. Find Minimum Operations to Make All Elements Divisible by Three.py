class Solution(object):
    def minimumOperations(self, nums):
        return sum(num % 3 > 0 for num in nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        r=0
        for i in nums:
            if i%3==0:
                r+=1
        return len(nums)-r
        """
        
                
        
