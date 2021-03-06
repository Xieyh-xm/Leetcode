'''
两数之和 II - 输入有序数组
给你一个下标从 1 开始的整数数组 numbers，该数组已按非递减顺序排列，请你从数组中找出满足相加之和等于目标数 target 的两个数。
如果设这两个数分别是 numbers [index1] 和 numbers [index2]，则 1 <=index1 <index2 <=numbers. Length。
以长度为 2 的整数数组[index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。你所设计的解决方案必须只使用常量级的额外空间。

输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
'''
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''方法一：哈希表'''
        # dict = {}
        # ans = []
        # for i, num in enumerate(numbers):
        #     if target - num in dict:
        #         ans.append(dict[target - num] + 1)
        #         ans.append(i + 1)
        #     else:
        #         dict[num] = i
        # return ans
        '''方法二：相向而行的双指针'''
        index_left, index_right = 0, len(numbers) - 1
        while index_left <= index_right:
            if numbers[index_left] + numbers[index_right] < target:
                index_left += 1
            elif numbers[index_left] + numbers[index_right] > target:
                index_right -= 1
            else:
                return [index_left + 1, index_right + 1]
