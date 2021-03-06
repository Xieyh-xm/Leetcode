'''
请你判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
---------------------------------------------
输入：board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true
---------------------------------------------
'''
import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''简单的一次遍历就好'''
        # 1. 新建三个哈希表
        row = [[0]*9 for _ in range(9)]
        columns = [[0]*9 for _ in range(9)]
        subboard = [[[0]*9 for _ in range(3)] for _ in range(3)]
        # 2. 遍历
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1
                row[i][num] += 1
                columns[j][num] += 1
                subboard[int(i / 3)][int(j / 3)][num] += 1
                if row[i][num] > 1 or columns[j][num] > 1 or subboard[int(i / 3)][int(j / 3)][num] > 1:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    nums = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = solution.isValidSudoku(nums)
    print(result)
