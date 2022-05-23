'''组合总和 II'''
from typing import List

'''会超时'''


# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         ret, path = [], []
#
#         def backtracking(startIdx):
#             if sum(path) > target:
#                 return
#             elif sum(path) == target:
#                 path_tmp = sorted(path)
#                 if path_tmp not in ret:
#                     ret.append(path_tmp)
#                 return
#             for i in range(startIdx, len(candidates)):
#                 path.append(candidates[i])
#                 backtracking(i + 1)
#                 path.pop()
#             return
#
#         backtracking(0)
#         return ret

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret, path = [], []

        def backtracking(startIdx, layer):
            if sum(path) > target:
                return
            elif sum(path) == target:
                ret.append(path[:])
                return
            # todo:可以再剪枝一下
            for i in range(startIdx, len(candidates)):
                if i > startIdx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtracking(i + 1, layer + 1)
                path.pop()
            return
        # 树层去重，要对数组进行排序
        candidates = sorted(candidates)
        backtracking(0, layer=0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
