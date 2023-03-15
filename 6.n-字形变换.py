# @before-stub-for-debug-begin
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step = (numRows - 1) * 2
        sub_row_lens = [len(s) // step] * step
        for i in range(len(s) % step):
            sub_row_lens[i] += 1
        offsets = [0] * step
        row_offset = 0
        for row in range(numRows):
            if row == 0:
                offsets[0] = 0
                row_offset += sub_row_lens[0]
            elif row == numRows - 1:
                offsets[row] = row_offset
            else:
                pair = step - row
                offsets[row] = row_offset
                offsets[pair] = offsets[row] + 1
                row_offset += sub_row_lens[row] + sub_row_lens[pair]
        # build result
        result = [None] * len(s)
        for i, ch in enumerate(s):
            i %= step
            result[offsets[i]] = ch
            offsets[i] += 1 if i ==  0 or i == numRows - 1 else 2
        return ''.join(result)


# print(Solution().convert('PAYPALISHIRING', 3))
# print(Solution().convert('PAYPALISHIRING', 4))
# print(Solution().convert('A', 1))
# @lc code=end

