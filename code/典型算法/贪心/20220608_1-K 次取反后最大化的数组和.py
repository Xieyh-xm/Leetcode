'''K 次取反后最大化的数组和'''

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx = 0  # 指向数组中的最小元素
        ans = sum(nums)
        for i in range(k):
            if nums[idx] < 0:
                ans += 2 * abs(nums[idx])
                nums[idx] = -nums[idx]
                if idx + 1 < len(nums) and nums[idx] > nums[idx + 1]:
                    idx += 1
            elif nums[idx] > 0:
                ans -= 2 * nums[idx]
                nums[idx] = -nums[idx]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.largestSumAfterKNegations([-2, 9, 9, 8, 4], k=5))
