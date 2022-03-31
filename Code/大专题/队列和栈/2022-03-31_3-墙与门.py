'''
墙与门
你被给定一个 m×n 的二维网格 rooms，网格中有以下三种可能的初始化值：
1. -1 表示墙或是障碍物
2.0 表示一扇门
3.INF 无限表示一个空的房间。然后，我们用 231-1=2147483647 代表 INF。你可
以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到最近门的距离，如果无法到达门，则填 INF 即可。

输入：rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
输出：[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
'''

from typing import List

'''
我们先搜索表格，把所有的门放入栈中。
每次遍历时，把栈中的点全部弹出，然后各自搜索相邻的格子。把相邻的格子再入栈。这样，就能多源地同时搜索。
当某一次搜索没有找到任何一个可入栈的新格子时，说明能够到达门的格子已经都被搜索过了，直接结束即可。

作者：accsrd
链接：https://leetcode-cn.com/problems/walls-and-gates/solution/python3-jian-dan-de-bfs-by-accsrd-1152/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 多源BFS 妙啊
# 把所有门都找出来， 对所有门，使用队列，同时都走了1步，
# 先到达的就是距离短的(并不是对一扇门进行BFS到底)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ###### 多源BFS
        INF = 2147483647
        Row = len(rooms) # 行数
        if Row == 0:
            return 
        Col = len(rooms[0]) # 列数

        queue = []
        for r in range(Row):
            for c in range(Col):
                if rooms[r][c] == 0:    #从门开始
                    queue.append((r, c, 0))
        while queue:
            r, c, dist = queue.pop(0) # 关键
            for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < Row and 0 <= nc < Col and rooms[nr][nc] == INF:    #是空的房间
                    rooms[nr][nc] = dist + 1
                    queue.append( (nr, nc, dist + 1) )  # 关键