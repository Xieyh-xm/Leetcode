'''N 皇后'''

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret, path = [], []

        used = [False for k in range(n)]
        # 转换为题目所需表达
        def num2Str(num) -> str:
            ret = ""
            for i in range(n):
                if i == num:
                    ret += 'Q'
                else:
                    ret += '.'
            return ret
        # 确定是否符合条件
        def isValid(row, col):
            # check col
            for i, val in enumerate(path):
                if col == val:
                    return False
            # check 45
            for i in range(len(path)):
                if path[-1 - i] == col - i - 1:
                    return False
            # check 135
            for i in range(len(path)):
                if path[-1 - i] == col + i + 1:
                    return False
            return True
        # 回溯
        def backtracking(row) -> None:
            if row >= n:
                tmp = []
                for i in range(len(path)):
                    tmp.append(num2Str(path[i]))
                ret.append(tmp[:])
                return
            for i in range(n):  # i代表列
                if used[i]:
                    continue
                if isValid(row, i):
                    used[i] = True
                    path.append(i)
                    backtracking(row + 1)
                    path.pop()
                    used[i] = False
            return

        backtracking(0)
        return ret


if __name__ == '__main__':
    solutio = Solution()
    print(solutio.solveNQueens(4))
