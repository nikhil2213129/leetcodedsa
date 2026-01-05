class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        hash = set()
        for i in nums:
            if i in hash:
                return i
            else:
                hash.add(i)
        o(n) time complexity
        o(n) space complexity
        """
        # Floyd's cycle detection algorithm
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
