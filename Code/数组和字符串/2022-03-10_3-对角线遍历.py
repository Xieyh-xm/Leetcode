'''
对角线遍历
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
---------------------------------------------
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
---------------------------------------------
'''
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        row, col = len(mat), len(mat[0])
        cnt = row + col - 1
        dir = True  # True向上，False向下
        cur_row, cur_col = 0, 0
        for i in range(cnt):
            while 1:
                ans.append(mat[cur_row][cur_col])
                if dir:
                    if cur_row - 1 < 0 or cur_col + 1 >= col:
                        break
                    cur_row -= 1
                    cur_col += 1
                else:
                    if cur_col - 1 < 0 or cur_row + 1 >= row:
                        break
                    cur_row += 1
                    cur_col -= 1
            if dir:
                if cur_col + 1 >= len(mat[0]):
                    cur_row += 1
                else:
                    cur_col += 1
            else:
                if cur_row + 1 == len(mat):
                    cur_col += 1
                else:
                    cur_row += 1
            dir = not dir
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDiagonalOrder([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]))
