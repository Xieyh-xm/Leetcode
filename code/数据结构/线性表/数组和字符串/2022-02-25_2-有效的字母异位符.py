'''
有效的字母异位符
给定两个字符串 s 和 t，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：1. 若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
     2. s 和 t 仅包含小写字母
---------------------------------------------
输入: s = "anagram", t = "nagaram"
输出: true
---------------------------------------------
进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = collections.Counter()
        for i in range(len(s)):
            letter_s = ord(s[i])
            letter_t = ord(t[i])
            m[letter_t] += 1
            m[letter_s] -= 1
        for num in m:
            if m[num] < 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(str(solution.isAnagram("anagram", "nagarlm")))
