'''
岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
'''

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:    
        row,col=len(grid),len(grid[0])
        ans=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    ans+=1
                    queue=[]
                    queue.append((i,j))
                    grid[i][j]='0'
                    while queue:
                        r,c=queue.pop()
                        for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:
                            nr,nc=r+dr,c+dc
                            if 0<=nr<row and 0<=nc<col and grid[nr][nc]=='1':
                                queue.append((nr,nc))
                                grid[nr][nc]='0'
        return ans
        
if __name__=='__main__':
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    s=Solution()
    print(s.numIslands(grid))
        
        
        