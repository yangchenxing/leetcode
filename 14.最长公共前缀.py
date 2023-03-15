#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
# from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        min_len = len(strs[0])
        sample = strs[0]
        for s in strs:
            if len(s) < min_len:
                sample = s
                min_len = len(sample)
        if min_len == 0:
            return ''
        for p in range(len(sample)):
            ch = sample[p]
            for s in strs:
                if s[p] != ch:
                    return sample[:p]
            p += 1
        return sample[:p]


# print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
# print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
# print(Solution().longestCommonPrefix([]))
# @lc code=end
