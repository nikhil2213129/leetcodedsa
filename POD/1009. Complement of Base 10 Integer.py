class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        while mask < n:
            mask = (mask << 1) | 1  # changed + to | for bitwise OR
        return mask ^ n
