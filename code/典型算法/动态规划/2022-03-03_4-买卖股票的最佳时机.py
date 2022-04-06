'''
买卖股票的最佳时机
给定一个数组 prices，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。
设计一个算法来计算你所能获取的最大利润。返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0。
---------------------------------------------
输入：prices = [7,6,4,3,1]
输出：0
---------------------------------------------
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        max_profit = 0
        # for price in prices:
        #     if price < min_prices:
        #         min_prices = prices
        #     elif price - min_prices > max_profit:
        #         max_profit = price - min_prices
        # return max_profit

        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            elif prices[i] - min_prices > max_profit:
                max_profit = prices[i] - min_prices
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 4]))
