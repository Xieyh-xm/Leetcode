'''递增子序列'''

from typing import List


#
# class Solution:
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         ret, path = [], []
#
#         def check(sub_seq: List):
#             if len(sub_seq) < 2:
#                 return False
#             for i in range(1, len(sub_seq)):
#                 if sub_seq[i] < sub_seq[i - 1]:
#                     return False
#             return True
#
#         def backtracking(startIdx):
#             if startIdx >= len(nums):
#                 return
#             for i in range(startIdx, len(nums)):
#                 path.append(nums[i])
#                 if check(path) and path not in ret:
#                     ret.append(path[:])
#                 backtracking(i + 1)
#                 path.pop()
#
#         backtracking(0)
#         return ret


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ret, path = [], []

        def check(sub_seq: List):
            if len(sub_seq) < 2:
                return False
            for i in range(1, len(sub_seq)):
                if sub_seq[i] < sub_seq[i - 1]:
                    return False
            return True

        def backtracking(startIdx):
            if startIdx >= len(nums):
                return
            used_flag = []  # 去除重复
            for i in range(startIdx, len(nums)):
                if nums[i] in used_flag:
                    continue
                path.append(nums[i])
                used_flag.append(nums[i])
                if check(path):
                    ret.append(path[:])
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubsequences([4, 6, 7, 7]))
