'''
罗马数字转整数
给定一个罗马数字，将其转换成整数。
---------------------------------------------
输入: s = "III"
输出: 3
---------------------------------------------
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5,
                "X": 10, "L": 50,
                "C": 100, "D": 500,
                "M": 1000}
        ans = 0
        for i in range(len(s)):
            ans += dict[s[i]]
            if i >= 1 and dict[s[i - 1]] < dict[s[i]]:
                ans -= 2 * dict[s[i - 1]]
        return ans
