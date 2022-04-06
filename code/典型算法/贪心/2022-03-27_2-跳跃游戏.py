'''
跳跃游戏
给定一个非负整数数组 nums，你最初位于数组的第一个下标。
数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个下标。

输入：nums = [2,3,1,1,4]
输出：true
'''

from typing import List

'''key:如果一个位置能够到达，那么这个位置左侧所有位置都能到达'''


# 1. 如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点
# 2. 可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新
# 3. 如果可以一直跳到最后，就成功了


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        for i in range(len(nums)):
            if i > idx:
                return False
            idx = max(idx, i + nums[i])
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
