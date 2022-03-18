'''
两个数组的交集
给定两个数组 nums1 和 nums2，返回它们的交集。输出结果中的每个元素一定是唯一的。我们可以不考虑输出结果的顺序。

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
'''
from re import S
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        haspMap_1=set(nums1)
        haspMap_2=set(nums2)
        return list(haspMap_1&haspMap_2)
