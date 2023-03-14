#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] 给定行和列的和求可行矩阵
#

# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [None] * len(rowSum)
        width = len(colSum)
        for r, rs in enumerate(rowSum):
            row = [0] * width
            for c, cs in enumerate(colSum):
                if cs == 0:
                    continue
                if rs == 0:
                    break
                row[c] = min(rs, cs)
                rs -= row[c]
                colSum[c] -= row[c]
            result[r] = row
        return result
# @lc code=end

