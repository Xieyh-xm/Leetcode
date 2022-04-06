'''
移动0
给定一个数组 nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
请注意，必须在不复制数组的情况下原地对数组进行操作。
---------------------------------------------
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
---------------------------------------------
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''方法一：双指针'''
        # 1. 先找到第1个0
        zero_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index = i
                break
        if zero_index == -1:
            return
        num_index = zero_index + 1
        # 2. 开始找
        while num_index < len(nums):
            if nums[num_index] != 0:
                nums[zero_index] = nums[num_index]
                nums[num_index] = 0
                zero_index += 1
            num_index += 1
        '''方法二：1. 把非0的都往前挪
                  2. 遍历完,剩余的位置全部用0补齐'''

if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    solution.moveZeroes(nums)
    print(nums)
