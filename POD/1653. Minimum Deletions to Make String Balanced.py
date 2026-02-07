class Solution(object):
    def minimumDeletions(self, s):
        ans = 0
        count = 0
        for x in s:
            if x == 'b':
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans
