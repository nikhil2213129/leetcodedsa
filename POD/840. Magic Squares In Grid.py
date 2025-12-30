class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        def is_magic(square):
            # Flatten the 3x3 grid
            nums = [num for row in square for num in row]
            # Must contain digits 1–9 exactly once
            if sorted(nums) != list(range(1, 10)):
                return False

            # Check rows, cols, diagonals
            target = 15
            for row in square:
                if sum(row) != target:
                    return False
            for c in range(3):
                if sum(square[r][c] for r in range(3)) != target:
                    return False
            if square[0][0] + square[1][1] + square[2][2] != target:
                return False
            if square[0][2] + square[1][1] + square[2][0] != target:
                return False

            return True

        count = 0
        # Slide 3x3 window
        for r in range(rows - 2):
            for c in range(cols - 2):
                square = [grid[r+i][c:c+3] for i in range(3)]
                if is_magic(square):
                    count += 1

        return count
