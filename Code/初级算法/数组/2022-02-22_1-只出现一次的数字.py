'''
只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''方法一：排序+判等'''
        # if len(nums) == 1:
        #     return nums[0]
        # # 1. 排序
        # nums.sort()
        # # 2. 计数
        # result = nums[0]
        # if nums[0] != nums[1]:
        #     result = nums[0]
        # elif nums[-2] != nums[-1]:
        #     result = nums[-1]
        # else:
        #     for i in range(1, len(nums) - 1):
        #         if nums[i - 1] != nums[i] and nums[i + 1] != nums[i]:
        #             result = nums[i]
        #             break
        # return result

        '''方法二：位运算
        注意：题目说了其余元素均只出现两次；异或运算具有交换律'''
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result
