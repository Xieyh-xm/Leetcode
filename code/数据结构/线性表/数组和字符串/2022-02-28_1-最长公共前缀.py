'''
最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串
---------------------------------------------
输入：strs = ["flower","flow","flight"]
输出："fl"
---------------------------------------------
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        j = 0
        while j < len(strs[0]):
            for i in range(len(strs)):  # 遍历一遍strs
                if j >= len(strs[i]):
                    return prefix
                if strs[i][j] != strs[0][j]:
                    return prefix
                if i == len(strs) - 1:
                    prefix += strs[i][j]
            j += 1
        return prefix


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["ower", "flow", "flight"]))
