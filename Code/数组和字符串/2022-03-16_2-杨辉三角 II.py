'''
杨辉三角 II
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

输入: rowIndex = 3
输出: [1,3,3,1]
'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def countNext(lastRow: List) -> List[int]:
            if len(lastRow) == 0:
                return [1]
            temp = [1]
            for i in range(1, len(lastRow)):
                temp.append(lastRow[i - 1] + lastRow[i])
            temp.append(1)
            return temp

        ans = [1]
        for i in range(rowIndex):
            ans = countNext(ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(1))
