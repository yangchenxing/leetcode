#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#

# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = [0] * n
        for a, b in roads:
            d[a] += 1
            d[b] += 1
        max_d = max(d)
        cities = [i for i, v in enumerate(d) if v == max_d]
        if len(cities) == 1:
            best_city = cities[0]
            max_d_2 = max(v for v in d if v < max_d)
            count_max_d_2 = sum(1 for v in d if v == max_d_2)
            for a, b in roads:
                if a == best_city and d[b] == max_d_2 or b == best_city and d[a] == max_d_2:
                    count_max_d_2 -= 1
            return max_d + max_d_2 - (0 if count_max_d_2 else 1)
        else:
            cities = set(cities)
            pairs = sum(1 for a, b in roads if a in cities and b in cities)
            return max_d * 2 - (0 if pairs < len(cities) * (len(cities) - 1) / 2 else 1)
# @lc code=end

