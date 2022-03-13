'''
搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
---------------------------------------------
输入: nums = [1,3,5,6], target = 5
输出: 2
---------------------------------------------
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''二分法+递归'''
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums: List[int], min_idx, max_idx, target):
        if min_idx >= max_idx:
            if nums[min_idx] < target:
                return min_idx + 1
            return min_idx
        mid_idx = (min_idx + max_idx) // 2
        if nums[mid_idx] > target:
            return self.binarySearch(nums, min_idx, mid_idx - 1, target)
        elif nums[mid_idx] < target:
            return self.binarySearch(nums, mid_idx + 1, max_idx, target)
        else:
            return mid_idx


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1], 0))
