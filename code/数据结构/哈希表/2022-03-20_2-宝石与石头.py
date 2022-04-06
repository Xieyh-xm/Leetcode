'''
宝石与石头

给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。
stones 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
字母区分大小写，因此“a”和“A”是不同类型的石头。

输入：jewels = "aA", stones = "aAAbbbb"
输出：3
'''



class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        m=set()
        for val in jewels:
            m.add(val)
        count=0
        for val in stones:
            if val in m:
                count+=1
        return count