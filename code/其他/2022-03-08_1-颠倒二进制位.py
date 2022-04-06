'''
颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。
---------------------------------------------
输入：n = 00000010100101000001111010011100
输出：964176192 (00111001011110000010100101000000)
---------------------------------------------
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = ans << 1
            ans += n & 1
            n = n >> 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.reverseBits("")
