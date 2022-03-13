'''
翻转字符串里的单词
给你一个字符串 s，逐个翻转字符串中的所有单词。
单词是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的单词分隔开。
请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。
---------------------------------------------
输入：s = "the sky is blue"
输出："blue is sky the"
---------------------------------------------
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        ''' 双指针算法 '''
        ans = ""
        s = s + ' '  # 后面加一个空格
        index_left, index_right = len(s) - 1, len(s) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' or i == 0:
                index_left = i
                if s[index_right - 1] == ' ':  # 处理多个空格的情况
                    index_right -= 1
                else:
                    if index_left != index_right:  # 处理多个空格的情况
                        if s[i] != ' ' and i == 0:  # 处理开头没空格的情况
                            ans += ' ' + s[index_left:index_right]
                        else:
                            ans += s[index_left:index_right]
                        index_right = index_left
        ans = ans[1:]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords(" asdasd df f"))
