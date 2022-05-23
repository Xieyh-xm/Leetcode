'''组合总和'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret, path = [], []

        def backtracking(startIdx):
            if startIdx >= len(candidates):
                return
            if sum(path) == target:
                ret.append(path[:])
                return
            elif sum(path) > target:
                return
            for i in range(startIdx, len(candidates)):
                path.append(candidates[i])
                backtracking(i)
                path.pop()
            return

        backtracking(0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
