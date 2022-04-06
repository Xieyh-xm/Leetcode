'''
岛屿的周长
给定一个 row×co1 的二维网格地图 grid，其中：grid [i] [j] =1 表示陆地，grid [i] [j] -0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。
整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）
岛屿中没有”湖”（（“湖”指水域在岛屿内部且不和岛屿周围的水相连）。
格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100。计算这个岛屿的周长。

输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边
'''

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''每有一个接壤的，减2条'''
        border=0
        row,col=len(grid),len(grid[0])
        haspSet=[]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    queue=[]
                    queue.append((i,j))
                    grid[i][j]=0
                    haspSet.append(str((i,j)))
                    while queue:
                        r,c=queue.pop()
                        for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:
                            nr,nc=dr+r,dc+c
                            if not (0<=nr<row and 0<=nc<col):
                                border+=1
                            elif grid[nr][nc]==0:
                                if str((nr,nc)) in haspSet:
                                    continue
                                border+=1
                            else:
                                grid[nr][nc]=0
                                queue.append((nr,nc))
                                haspSet.append(str((nr,nc)))
        return border
    
if __name__=='__main__':
    s=Solution()
    print(s.islandPerimeter([[1,1],[1,1]]))