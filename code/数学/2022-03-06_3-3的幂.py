'''
3的幂
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

---------------------------------------------
输入：n = 27
输出：true
---------------------------------------------
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 3 == 0:
                n = n / 3
            else:
                return False
        return True
