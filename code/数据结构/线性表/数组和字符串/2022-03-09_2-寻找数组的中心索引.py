'''
寻找数组的中心索引
给你一个整数数组 nums，请计算数组的中心下标。
数组中心下标是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
如果中心下标位于数组最左端，那么左侧数之和视为 0，因为在下标的左侧不存在元素。
这一点对于中心下标位于数组最右端同样适用。如果数组有多个中心下标，应该返回最靠近左边的那一个。如果数组不存在中心下标，返回-1。
---------------------------------------------
输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
---------------------------------------------
'''

'''
想太多的时候注意审题，题目的规定限制了奇怪答案的出现
注意注意：如果数组有多个中心下标，应该返回 最靠近左边 的那一个。
'''
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        left_sum = 0
        for idx in range(len(nums)):
            if left_sum * 2 + nums[idx] == sum:
                return idx
            left_sum += nums[idx]
        return -1
