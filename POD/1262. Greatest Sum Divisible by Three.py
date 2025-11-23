
class Solution:
    def maxSumDivThree(self, nums):
        import sys
        a = sys.maxsize
        b = sys.maxsize
        c = sys.maxsize
        d = sys.maxsize
        s = 0
        for i in nums:
            s += i
            if i % 3 == 1:
                if i < a:
                    b = a
                    a = i
                elif i < b:
                    b = i
            elif i % 3 == 2:
                if i < c:
                    d = c
                    c = i
                elif i < d:
                    d = i
        if s % 3 == 0:
            return s
        if s % 3 == 1:
            ans = 0
            if a != sys.maxsize:
                ans = s - a
            if d != sys.maxsize and c != sys.maxsize:
                ans = max(ans, s - d - c)
            return ans
        ans = 0
        if c != sys.maxsize:
            ans = s - c
        if a != sys.maxsize and b != sys.maxsize:
            ans = max(ans, s - a - b)
        return ans
