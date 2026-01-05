class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int

        """
        totalsum = 0
        minabsvalue = float('inf')
        negativecount = 0
        for row in matrix:
            for val in row:
                totalsum += abs(val)
                if val<0:
                    negativecount += 1
                minabsvalue = min(minabsvalue,abs(val))
        if negativecount %2 != 0:
            totalsum -= 2*minabsvalue
        return totalsum
