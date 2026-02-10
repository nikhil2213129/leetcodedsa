class Solution(object):

    def longestBalanced(self, nums):
        if len(nums) <= 1:
            return 0
        
        # len >= 2
        max_len = 0
        
        for end in range(len(nums) - 1, 0, -1):
            # Find max length with end index and start index is from 0..end-1
            
            if max_len >= end + 1:  # longest array when start = 0
                break  # no longer need to continue
            
            even_set = set()
            odd_set = set()
            
            # Init regarding the current max_len: only search for longer arrays
            restricted_end = end - max_len + 1
            for pos in range(end, restricted_end - 1, -1):
                if nums[pos] % 2 == 0:
                    even_set.add(nums[pos])
                else:
                    odd_set.add(nums[pos])
            
            for start in range(restricted_end - 1, -1, -1):
                if nums[start] % 2 == 0:
                    even_set.add(nums[start])
                else:
                    odd_set.add(nums[start])
                
                if len(even_set) == len(odd_set):
                    max_len = end - start + 1
        
        return max_len
