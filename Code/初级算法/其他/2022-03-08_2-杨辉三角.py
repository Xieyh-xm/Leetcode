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