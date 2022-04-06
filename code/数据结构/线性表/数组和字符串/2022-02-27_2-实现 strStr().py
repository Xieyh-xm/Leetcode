'''
实现 strStr()
实现 strStr0 函数。
给你两个字符串 haystack 和 needle，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回-1。当 needle 是空字符串时我们应当返回 0
---------------------------------------------
输入：haystack = "hello", needle = "ll"
输出：2

输入：haystack = "aaaaa", needle = "bba"
输出：-1

输入：haystack = "", needle = ""
输出：0
---------------------------------------------
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''方法一：朴素解法 / 会超出时间限制'''
        if len(needle) == 0:
            return 0
        elif len(haystack) < len(needle):
            return -1
        i, j = 0, 0
        index = -1
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if index == -1:
                    index = i
                j = j + 1
                if j >= len(needle):
                    return index
            else:
                if index != -1:
                    i = index   # 回溯消耗大量时间
                    index = -1
                    j = 0
            i += 1
        return -1

        '''方法二：KMP算法...再说吧'''


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("mississippi", "issipi"))
