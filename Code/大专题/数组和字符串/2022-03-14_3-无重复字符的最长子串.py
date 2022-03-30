'''
无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''方法二：滑动窗口'''
        maxLength = 0
        dict = {}
        index_left = 0
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= index_left:
                index_left = dict[s[i]] + 1
                dict[s[i]] = i
            else:
                dict[s[i]] = i
            maxLength = max(maxLength, i - index_left + 1)
        return maxLength
        '''方法一：暴力解法'''
        # def longestSubstring(s: str, index):
        #     length = 0
        #     m = collections.Counter()
        #     i = 0
        #     while index + i < len(s) and m[s[index + i]] < 1:
        #         m[s[index + i]] += 1
        #         length += 1
        #         i += 1
        #     return length
        #
        # maxLength = 0
        # for i in range(len(s)):
        #     cur_length = longestSubstring(s, i)
        #     if maxLength < cur_length:
        #         maxLength = cur_length
        #     i += 1
        # return maxLength


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abba"))
