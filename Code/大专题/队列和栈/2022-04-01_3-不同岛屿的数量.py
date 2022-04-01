'''
不同岛屿的数量

给定一个非空 01 二维数组表示的网格.
一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。
请你计算这个网格中共有多少个形状不同的岛屿。
两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。

示例 1：
    11000
    11000
    00011
    00011
返回结果 1 。
'''

from typing import List

'''难点：怎么判断岛屿的形状是否相同？

'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        hashMap={}
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    path="00"
                    queue=[]
                    queue.append((i,j))
                    while queue:
                        r,c=queue.pop()
                        for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:
                            nr,nc=dr+r,dc+c
                            if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                                queue.append((nr,nc))
                                path+=str(nr-i)+str(nc-j)
                                grid[nr][nc]=0
                    if path not in hashMap:
                        hashMap[path]=1
        return len(hashMap)