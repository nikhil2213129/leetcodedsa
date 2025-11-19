class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        
        ptr = 0
        while ptr<len(nums):
            if nums[ptr] == original:
                #nums[ptr] = 2*original
                original = 2*original
                ptr = 0
            else:
                ptr+=1
        return original 
        """
        # Convert the list to a set for O(1) lookup time
        nums_set = set(nums)
      
        # Keep doubling the original value while it exists in the set
        while original in nums_set:
            # Left shift by 1 is equivalent to multiplying by 2
            original = original << 1
      
        # Return the final value after all doublings
        return original
