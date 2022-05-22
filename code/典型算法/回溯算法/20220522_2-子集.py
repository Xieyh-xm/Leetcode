'''子集'''

from typing import List


# 类似组合
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret, path = [], []

        def backtracking(startIdx) -> None:
            if startIdx >= len(nums):
                return
            for i in range(startIdx, len(nums)):
                path.append(nums[i])
                # if path not in ret:
                #     ret.append(path[:])
                ret.append(path[:])
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        ret.append([])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
