class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        n = len(nums)
        # d represents the distance from the start index
        for d in range(n):
            # Check left side: start - d
            if start - d >= 0 and nums[start - d] == target:
                return d
            # Check right side: start + d
            if start + d < n and nums[start + d] == target:
                return d
        return -1
