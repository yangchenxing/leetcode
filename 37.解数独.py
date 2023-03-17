#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
from typing import *
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

from collections import deque

class Solution:
    founds = {
        0b1: '1',
        0b10: '2',
        0b100: '3',
        0b1000: '4',
        0b10000: '5',
        0b100000: '6',
        0b1000000: '7',
        0b10000000: '8',
        0b100000000: '9',
    }

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cells = [[0b111111111] * 9 for i in range(9)]
        digits = [[0b111111111] * 9 for i in range(9)]
        queue = deque()
        # init cells
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == '.':
                    continue
                else:
                    Solution.disable(board, cells, i, j, 1 << (ord(ch) - 49), queue)
                        
        # process
        while queue:
            print(len(queue))
            i, j = queue.pop()
            if board[i][j] != '.':
                continue
            board[i][j] = Solution.founds[cells[i][j]]
            print_board(board)
            Solution.disable(board, cells, i, j, cells[i][j], queue)
            

    @staticmethod
    def disable(board, cells, i, j, mark, queue):
        mark = 0b111111111 ^ mark
        # disable by ocurr
        for x in range(9):
            if x != j:
                cells[i][x] &= mark
                if cells[i][x] in Solution.founds and board[i][x] == '.':
                    queue.append((i, x))
            if x != i:
                cells[x][j] &= mark
                if cells[x][j] in Solution.founds and board[x][j] == '.':
                    queue.append((x, j))
        r0 = i // 3 * 3
        c0 = j // 3 * 3
        for r in range(3):
            r += r0
            for c in range(3):
                c += c0
                if r == i and c == j:
                    continue
                cells[r][c] &= mark
                if cells[r][c] in Solution.founds and board[r][c] == '.':
                    queue.append((r, c))
        # disable by 
        
s = Solution()
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# s.solveSudoku(board)
# for row in board:
#     print(' '.join(row))
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print_board(board)
print()
s.solveSudoku(board)
print_board(board)                
# @lc code=end

