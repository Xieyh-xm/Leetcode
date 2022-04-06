'''
最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
---------------------------------------------
输入：s = "babad"
输出："bab"
---------------------------------------------
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''动态规划：以空间换时间'''
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        index = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # 递推开始
        # 先枚举子串长度，L代表子串长度，短的子串先来
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                j = L + i - 1
                # 左边界越界，直接退出
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] == True and j - i + 1 > max_len:
                    max_len = j - i + 1
                    index = i
        return s[index:index + max_len]
