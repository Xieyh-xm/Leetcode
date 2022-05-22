'''单词长度的最大乘积'''
from collections import defaultdict
from functools import reduce
from itertools import product
from typing import List


# 思路：位运算
# 如果能将判断两个字符是否有公共字符的复杂度降到O(1),则可以将总时间复杂度降低到O(n^2)
# 可以使用位运算预处理每个单词，通过位运算操作判断两个单词是否有公共字母。
# 光是reduce一句就可以学半天...

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # reduce() 函数会对参数序列中元素进行累积。
        # 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
        # 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
        masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
        # 如果有多个单词的位掩码相同，则只需要记录该位掩码对应的最大单词长度即可。
        dict = defaultdict(int)
        for i, word in enumerate(words):
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0)
            dict[mask] = max(len(words[i]), dict[mask])
        ans = 0
        for x, y in product(dict, repeat=2):
            if x & y == 0:
                ans = max(dict[x] * dict[y], ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct(["a", "aa", "aaa", "aaaa"]))
