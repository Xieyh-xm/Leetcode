'''
字符串中的第一个唯一字符
给定一个字符串 s，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回-1。
---------------------------------------------
输入: s = "leetcode"
输出: 0
---------------------------------------------
'''
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''方法一：遍历'''

        '''方法二：哈希表？'''
        m = collections.Counter(s)
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1
