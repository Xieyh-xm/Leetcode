'''
杨辉三角
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
---------------------------------------------
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
---------------------------------------------
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''把三角形拉直'''
        ans = [[1]]
        for i in range(1, numRows):
            num = i + 1  # 每层元素个数
            row = [1]
            for j in range(1, num - 1):
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            row.append(1)
            ans.append(row)
        return ans
