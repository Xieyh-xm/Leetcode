'''
缺失数字
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
---------------------------------------------
输入：nums = [3,0,1]
输出：2
---------------------------------------------
'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans + i - nums[i]
        ans = ans + len(nums)
        return ans
