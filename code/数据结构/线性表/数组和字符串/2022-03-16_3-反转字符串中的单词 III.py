'''
反转字符串中的单词 III
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        s += ' '
        ans = ""
        # 需要3个指针
        index_left = -1
        for index_blank, letter in enumerate(s):
            if letter == " ":
                # 找到空格，开始反转
                for i in range(index_blank, index_left, -1):
                    ans += s[i]
                index_left = index_blank
        return ans[1:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("Let's take LeetCode contest"))
