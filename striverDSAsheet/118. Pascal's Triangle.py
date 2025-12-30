class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        # Recursion method
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        previous_row = self.generate(numRows-1)
        newRow = [1]*numRows

        for i in range(1,numRows-1):
            newRow[i] = previous_row[-1][i-1]+previous_row[-1][i]
        previous_row.append(newRow)
        return previous_row
        
        """
        # Combinatorial Formula
        result = []
        if numRows == 0:
            return result
        first_row = [1]
        result.append(first_row)

        for i in range(1,numRows):
            prev_row = result[i-1]
            curr_row = [1]
            for j in range(1,i):
                curr_row.append(prev_row[j-1]+prev_row[j])
            curr_row.append(1)
            result.append(curr_row)
        return result


        
