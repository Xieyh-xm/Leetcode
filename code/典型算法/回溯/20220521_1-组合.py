'''
组合
'''
from typing import List

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ret, path = [], []
#
#         def backTracking(startidx) -> None:
#             print("startidx = ", startidx)
#             if len(path) == k:
#                 ret.append(path[:])
#                 return
#             for i in range(startidx, n + 1):
#                 path.append(i)
#                 backTracking(i + 1)
#                 path.pop()
#             return
#
#         backTracking(1)
#         return ret


'''剪枝优化'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret, path = [], []

        def backTracking(startidx) -> None:
            print("startidx = ", startidx)
            if len(path) == k:
                ret.append(path[:])
                return
            for i in range(startidx, n - (k - len(path))+2):
                path.append(i)
                backTracking(i + 1)
                path.pop()
            return

        backTracking(1)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
