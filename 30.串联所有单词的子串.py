#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
# from typing import *
from collections import defaultdict, deque

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        return list(Solution.search_all(s, len(words[0]), len(words), counts))

    def search_all(s, width, total_count, counts):
        for i in range(width):
            for pos in Solution.search(s, i, width, total_count, counts):
                yield pos

    @staticmethod
    def search(s, start, width, total_count, counts):
        total_remain = total_count
        remains = {}
        remains.update(counts)
        chunks = deque()

        for i in range(start, len(s), width):
            token = s[i:i+width]
            remain = remains.get(token, None)
            if remain is not None:
                if remain > 0:
                    chunks.append(token)
                    remains[token] -= 1
                    total_remain -= 1
                else:
                    while chunks[0] != token:
                        remains[chunks.popleft()] += 1
                        total_remain += 1
                        start += width
                    chunks.popleft()
                    start += width
                    chunks.append(token)
                if total_remain == 0:
                    yield start
            else:
                chunks.clear()
                start = i + width
                total_remain = total_count
                remains.update(counts)

# s = Solution()
# print(s.findSubstring('barfoothefoobarman', ['foo', 'bar']))
# print(s.findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']))
# print(s.findSubstring('barfoofoobarthefoobarman', ['bar', 'foo', 'the']))
# @lc code=end

