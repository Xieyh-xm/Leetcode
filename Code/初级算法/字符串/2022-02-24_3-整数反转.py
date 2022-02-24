'''
整数反转
给你一个 32 位的有符号整数×，返回将×中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围，就返回 0。假设环境不允许存储 64 位整数（有符号或无符号）。
---------------------------------------------
输入：x = 123
输出：321

输入：x = -123
输出：-321
---------------------------------------------
'''


class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            flag = False
        abs_x = abs(x)
        # 判断有几位
        for i in range(32):
            if abs_x < pow(10, i):
                length = i
                break
        # 拆分+组合
        result = 0
        for i in range(length - 1, -1, -1):
            temp = abs_x // pow(10, i)
            abs_x = abs_x % pow(10, i)
            result += temp * pow(10, length - i - 1)
            if result > pow(2, 31) - 1:
                return 0
        if flag == False:
            result = -result
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123))
