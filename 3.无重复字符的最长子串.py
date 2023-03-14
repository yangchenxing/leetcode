#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        pos = [None] * 255
        left = 0
        result = 0
        for i, ch in enumerate(s):
            ch = ord(ch)
            if pos[ch] is not None:
                left = max(pos[ch] + 1, left)
            result = max(result, i - left + 1)
            pos[ch] = i
        return result

# @lc code=end

