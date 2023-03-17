#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
# from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for i in range(9)]
        cols = [[False] * 9 for i in range(9)]
        sqrs = [[False] * 9 for i in range(9)]

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == '.':
                    continue
                ch = ord(ch) - 49
                # row
                if rows[i][ch]:
                    return False
                rows[i][ch] = True
                # col
                if cols[j][ch]:
                    return False
                cols[j][ch] = True
                # sqr
                k = i // 3 * 3 + j // 3
                if sqrs[k][ch]:
                    return False
                sqrs[k][ch] = True
        return True

# s = Solution()
# print(s.isValidSudoku(
#     [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# ))
# print(s.isValidSudoku(
#     [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# ))

# @lc code=end

