''' 169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。'''
from typing import List

'''解法一：遍历O(n)哈希表'''
# from collections import defaultdict
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         lookup = defaultdict(int)
#         maj = 0
#         for i in nums:
#             lookup[i] += 1
#             if lookup[i] > maj:
#                 out = i
#                 maj = lookup[i]
#         return out


'''解法二：摩尔投票法'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

