'''最长连续递增序列
给定一个未经排序的整数数组，找到最长且连续递增的子序列，并返回该序列的长度。
连续递增的子序列可以由两个下标 1 和 x（1 <x）确定，
如果对于每个 1 <=i <r，都有 nums [i] <nums [i+1]，
那么子序列[nums [1], nums [1+1], ·. ·, nums [r-1], nums [r]]就是连续递增子序列。

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
'''
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLength = 1
        curLength = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curLength += 1
                maxLength = max(maxLength, curLength)
            else:
                curLength = 1
        return maxLength


if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1, 3, 5, 4, 7]))
