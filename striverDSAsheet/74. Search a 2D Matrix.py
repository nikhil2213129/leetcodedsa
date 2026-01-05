class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row = len(matrix) - 1   # start from last row
        while row >= 0:
            # check boundaries of the current row
            if matrix[row][0] <= target <= matrix[row][-1]:
                # target must be in this row, do a binary search
                left, right = 0, len(matrix[row]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False  # searched the row fully, not found

            # if target is smaller than the first element, move up
            if target < matrix[row][0]:
                row -= 1
            else:
                # target is larger than the last element, no need to check higher rows
                return False

        return False
