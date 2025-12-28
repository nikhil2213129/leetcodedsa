class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in grid:
            for j in i:
                if j<0:
                    result += 1
        return result

        
