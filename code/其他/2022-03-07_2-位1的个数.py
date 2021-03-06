'''
位1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
---------------------------------------------
输入：00000000000000000000000000001011
输出：3
---------------------------------------------
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n = n >> 1
        return ans
