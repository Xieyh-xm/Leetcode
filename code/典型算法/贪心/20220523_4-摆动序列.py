'''摆动序列'''

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        last_flag = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_flag = 'up'
            elif nums[i] < nums[i - 1]:
                cur_flag = 'down'
            else:
                cur_flag = last_flag
            if cur_flag != last_flag:
                ans += 1
                last_flag = cur_flag
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.wiggleMaxLength([0, 0]))
