'''
字符串转换整数 (atoi)
请你来实现一个 myAtoi (string s)函数，使其能将字符串转换成一个32位有符号整数（类似C/C+中的atoi函数）。

函数 myAtoi (string s）的算法如下：
1. 读入字符串并丢弃无用的前导空格
2. 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。确定最终结果是负数还是正数。如果两者都不存
在，则假定结果为正。
3. 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
4. 将前面步骤读入的这些数字转换为整数（即，“123"->123，“0032"->32)。如果没有读入数字，则整数为 0。必要时更改符
号（从步骤 2 开始）。
5. 如果整数数超过 32 位有符号整数范围[-2^31,2^31-1]，需要截断这个整数，使其保持在这个范围内。具体来说，小于
-2^31 的整数应该被固定为-2^31，大于 2^31-1 的整数应该被固定为 2^31-1。
6. 返回整数作为最终结果。
---------------------------------------------
输入：s = "42"
输出：42

输入：s = "4193 with words"
输出：4193

输入：s = "   -42"
输出：-42
---------------------------------------------
'''


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start_index = 0
        for i in range(len(s)):
            if s[i] == " ":
                start_index += 1
            else:
                break
        if start_index == len(s):
            return 0
        if s[start_index] == "-":
            flag = -1
            start_index += 1
        elif s[start_index] == "+":
            flag = 1
            start_index += 1
        else:
            flag = 1
        if start_index == len(s):
            return 0
        for i in range(start_index, len(s)):
            length = i - start_index + 1
            if s[i] < '0' or s[i] > '9':
                length -= 1
                break
        sum = 0
        if length == 0:
            return 0
        for i in range(length - 1, -1, -1):
            sum += int(s[start_index + i]) * pow(10, length - i - 1)

        sum = sum * flag
        sum = min(sum, pow(2, 31) - 1)
        sum = max(sum, -pow(2, 31))
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi(" "))
