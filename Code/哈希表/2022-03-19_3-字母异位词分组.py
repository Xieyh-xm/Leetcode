'''
字母异位词分组
给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。
字母异位词是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

from ast import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=collections.defaultdict(list)
        for st in strs:
            '''排序'''
            cur="".join(sorted(st))
            hashMap[cur].append(st)
        return list(hashMap.values())
