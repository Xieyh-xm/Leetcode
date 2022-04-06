'''
给定一个 n×n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
---------------------------------------------
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
---------------------------------------------
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''1. 直接交换'''
        # for i in range(int(len(matrix) / 2)):

        '''2. 先上下交换，然后对角线交换'''
        # 上下交换
        for i in range(int(len(matrix) / 2)):
            for j in range(len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[-i - 1][j]
                matrix[-i - 1][j] = temp
        # 主对角线交换
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
