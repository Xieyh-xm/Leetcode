'''全排列'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret, path = [], []
        used = [False for i in range(len(nums))]

        def backtracking(used) -> None:
            if len(path) == len(nums):
                ret.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(used)
                used[i] = False
                path.pop()

        backtracking(used)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
