'''全排列 II'''

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret, path = [], []
        # 树枝去重
        used = [False for k in range(len(nums))]

        def backtracking(used):
            if len(path) == len(nums):
                ret.append(path[:])
                return
            used_layer = []      # 树层去重
            for i in range(len(nums)):
                if used[i] or nums[i] in used_layer:
                    continue
                used_layer.append(nums[i])  # 树层去重
                used[i] = True  # 树枝去重
                path.append(nums[i])
                backtracking(used)
                path.pop()
                used[i] = False
            return

        backtracking(used)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))
