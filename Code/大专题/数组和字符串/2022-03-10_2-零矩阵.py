'''
零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
---------------------------------------------
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
---------------------------------------------
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        # 置0
        for i in range(len(row)):
            matrix[row[i]] = [0] * len(matrix[0])
            for j in range(len(matrix)):
                matrix[j][col[i]] = 0
