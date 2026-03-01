class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        for i in range(9,-1,-1):
            if str(i) in n:
                return i
