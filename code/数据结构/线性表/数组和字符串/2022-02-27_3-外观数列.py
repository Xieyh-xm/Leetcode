'''
外观数列
给定一个正整数 n，输出外观数列的第 n 项。
外观数列是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     ......
---------------------------------------------
输入：n = 1
输出："1"
解释：这是一个基本样例。

输入：n = 4
输出："1211"
解释：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"
---------------------------------------------
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(1, n):
            result = self.countAndSay_sub(result)
        return result

    def countAndSay_sub(self, s: str) -> str:
        result = ""
        lastNum = s[0]  # 记录上一个数字
        # curNum = None  # 指示数字
        count = 1  # 给数字计数
        if len(s) == 1:
            return "11"
        for i in range(1, len(s)):
            curNum = s[i]
            if curNum == lastNum:
                count += 1
            else:
                # 先把前一个处理好
                result += str(count) + lastNum
                # 更新变量
                count = 1
                lastNum = curNum
        result += str(count) + lastNum
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(4))
