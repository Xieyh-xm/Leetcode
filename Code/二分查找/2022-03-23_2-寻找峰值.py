'''
寻找峰值
峰值元素是指其值严格大于左右相邻值的元素。
数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2
'''

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int: