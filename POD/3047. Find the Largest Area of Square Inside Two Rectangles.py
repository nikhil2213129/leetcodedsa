class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]
            for j in range(i+1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]
                width = min(x2, x4) - max(x1, x3)
                height = min(y2, y4) - max(y1, y3)
                side = min(width, height)
                if side > 0:
                    ans = max(ans, side * side)
        return ans
