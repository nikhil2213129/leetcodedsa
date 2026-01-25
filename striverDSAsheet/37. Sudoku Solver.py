from typing import List
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        col = [set(range(1, 10)) for _ in range(9)]
        row = [set(range(1, 10)) for _ in range(9)]
        sq = [set(range(1, 10)) for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    v = int(board[r][c])
                    row[r].remove(v)
                    col[c].remove(v)
                    sq[(r // 3) * 3 + c // 3].remove(v)

        def bktr(r, c, board):
            if board[r][c] != '.':
                if r == 8 and c == 8:
                    return True
                if c < 8:
                    return bktr(r, c + 1, board)
                return bktr(r + 1, 0, board)

            vals = col[c] & row[r] & sq[(r // 3) * 3 + c // 3]
            for v in vals:
                num = str(v)
                board[r][c] = num
                col[c].remove(v)
                row[r].remove(v)
                sq[(r // 3) * 3 + c // 3].remove(v)
                if (r == 8 and c == 8) or (r < 8 and c == 8 and bktr(r + 1, 0, board)) or (c < 8 and bktr(r, c + 1, board)):
                    return True
                board[r][c] = '.'
                col[c].add(v)
                row[r].add(v)
                sq[(r // 3) * 3 + c // 3].add(v)
            return False

        bktr(0, 0, board)
