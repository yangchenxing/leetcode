#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        j = len(x) - 1
        for i in range(len(x) // 2):
            if x[i] != x[j-i]:
                return False
        return True
# @lc code=end

