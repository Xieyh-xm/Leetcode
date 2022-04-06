'''
岛屿的最大面积
给你一个大小为 mxn 的二进制矩阵 grid
岛屿是由一些相邻的 1（代表土地）构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直的四个方向上相邻。
你可以假设 grid 的四个边缘都被（代表水）包围着。
岛屿的面积是岛上值为 1 的单元格的数目。
计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0。

输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
'''

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        row,col=len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    curArea=1
                    queue=[]
                    queue.append((i,j))
                    grid[i][j]=0
                    while queue:
                        r,c=queue.pop()
                        for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:
                            nr,nc=dr+r,dc+c
                            if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                                queue.append((nr,nc))
                                curArea+=1
                                grid[nr][nc]=0
                    maxArea=max(maxArea,curArea)
        return maxArea
    
if __name__=='__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    s=Solution()
    print(s.maxAreaOfIsland(grid))