class Solution:
    def trap(self, height):
        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = 0, 0
        res = 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    res += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    res += rightMax - height[right]
                right -= 1
        
        return res
