'''最大子数组和'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, sum = nums[0], 0
        for i, val in enumerate(nums):
            sum += val
            max_sum = max(sum, max_sum)
            if sum < 0:
                sum = 0
        return max_sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
