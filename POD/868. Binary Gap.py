class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)[2:]
        prev = -1
        dis = 0
        for curr in range(len(b)):
            if b[curr] == "1":
                if prev != -1:
                    dis = max(dis,curr-prev)
                prev = curr
        return dis
