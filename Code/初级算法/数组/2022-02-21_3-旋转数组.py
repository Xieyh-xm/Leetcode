from typing import List

'''
旋转数组
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。'''


# bug注意！k可能大于数组长度，需要取余

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法一：使用临时数组（不原地）
        # k = k % len(nums)
        # temp = list(range(len(nums)))
        # for i in range(len(nums)):
        #     if i < len(nums) - k:
        #         temp[k + i] = nums[i]
        #     else:
        #         temp[i + k - len(nums)] = nums[i]
        #
        # for i in range(len(nums)):
        #     nums[i] = temp[i]

        # 方法二：原地
        k = k % len(nums)
        # 1. 整体翻转
        for i in range(int(len(nums) / 2)):
            temp = nums[i]
            nums[i] = nums[-i - 1]
            nums[-i - 1] = temp
        # 2. 局部翻转两次
        for i in range(int((len(nums) - k) / 2)):
            temp = nums[i+k]
            nums[i+k] = nums[-i - 1]
            nums[-i - 1] = temp

        for i in range(int(k / 2)):
            temp = nums[i]
            nums[i] = nums[k - 1-i]
            nums[k - 1-i] = temp

if __name__ == '__main__':
    sulution = Solution()
    nums = [1, 2, 3, 4, 5]
    sulution.rotate(nums, 2)
    print(nums)
