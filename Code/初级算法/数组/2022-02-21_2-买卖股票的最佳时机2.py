'''
=====> 买卖股票的最佳时机 <=====
给定一个数组 prices，其中 prices[i] 表示股票第 i 天的价格。
在每一天，你可能会决定购买和/或出售股票。
你在任何时候最多只能持有一股股票。
你也可以购买它，然后在同一天出售。返回你能获得的最大利润。'''
# 贪心 数组 动态规划
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思路：将所有上升区间累加
        gain = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                gain = gain + prices[i + 1] - prices[i]
        return gain
