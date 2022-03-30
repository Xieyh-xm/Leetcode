'''
长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target。
找出该数组中满足其和≥target 的长度最小的连续子数组[nums1, nums1+1,, ·, numsr-1, numsr]，并返回其长度。如果不
存在符合条件的子数组，返回 0。
注意！！！是大于等于！！！

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''滑动窗口'''
        minLength = 0
        index_left, index_right = 0, 0
        cur_sum = nums[0]
        while index_right < len(nums):
            if cur_sum < target:
                index_right += 1
                if index_right >= len(nums):
                    break
                cur_sum += nums[index_right]
            else:
                if minLength == 0:
                    minLength = index_right - index_left + 1
                else:
                    minLength = min(minLength, index_right - index_left + 1)
                cur_sum -= nums[index_left]
                index_left += 1
        return minLength


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
