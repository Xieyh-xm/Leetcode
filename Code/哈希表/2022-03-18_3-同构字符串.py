'''
同构字符串
给定两个字符串 s 和七，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符
上，字符可以映射到自己本身。

输入：s = "egg", t = "add"
输出：true
'''

import collections
from operator import xor
from re import S
from unittest import main


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''维护两张哈希表'''
        dict1, dict2 = {}, {}
        for i in range(len(s)):
            if (s[i] in dict1) ^ (t[i] in dict2):
                return False
            if s[i] in dict1 and s[i] != dict2[t[i]]:
                return False
            dict1[s[i]] = t[i]
            dict2[t[i]] = s[i]
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
