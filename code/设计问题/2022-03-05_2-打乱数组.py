'''
打乱数组
给你一个整数数组 nums，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是等可能的。实现 Solution class:

- Solution (int [] nums) 使用整数数组 nums 初始化对象
- int [] reset() 重设数组到它的初始状态并返回
- int [] shuffle() 返回数组随机打乱后的结果

---------------------------------------------
输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
---------------------------------------------
'''
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.clone = nums

    def reset(self) -> List[int]:
        return self.clone

    def shuffle(self) -> List[int]:
        def swap(a, b):
            return b, a

        nums, array = [], []
        # 生成n个随机数
        for i in range(len(self.clone)):
            nums.append(random.random())
            array.append(self.clone[i])
        # 排序算法-冒泡排序
        for i in range(len(self.clone) - 1):
            for j in range(len(self.clone) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = swap(nums[j], nums[j + 1])
                    array[j], array[j + 1] = swap(array[j], array[j + 1])
        return array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
