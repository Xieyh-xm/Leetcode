'''
跳跃游戏 II
给你一个非负整数数组 nums，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。假设你总是可以到达数组的最后一个位置。

输入: nums = [2,3,1,1,4]
输出: 2
'''

from tracemalloc import start
from typing import List

# 每次在上次能跳到的范围（end）内选择一个能跳的最远的位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # end:跳跃右边界 超过时步数要+1
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:     #(其实可以不用)
                # max_jump为当前格子能跳最远距离 看是否超过当前的右边界
                maxPos = max(maxPos, i + nums[i])
                if i == end:    
                    # 达到当前右边界 右边界更新为边界之内所能跳的最远距离
                    # 右边界指上一次跳跃能跳到的最远距离
                    end = maxPos
                    # 下一次为一个新的起跳点 步数+1
                    step += 1
        return step