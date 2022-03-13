'''
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
---------------------------------------------
输入：s = "()"
输出：true
---------------------------------------------
'''


class Solution:
    def isValid(self, s: str) -> bool:
        '''栈+字典解决'''
        dict = {'(': ')', '{': '}', '[': ']'}
        bracket = []
        for letter in s:
            if letter == '(' or letter == '{' or letter == '[':
                bracket.append(letter)
            if letter == ')' or letter == '}' or letter == ']':
                if bracket == [] or letter != dict[bracket[-1]]:
                    return False
                else:
                    bracket = bracket[:-1]
        if len(bracket) != 0:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
