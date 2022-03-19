'''
四数相加 II
给你四个整数数组 nums1、nums2、nums3 和 nums4, 数组长度都是 n.
请你计算有多少个元组（i, j, k,1) 能满足：
    · 0 <=i, j, k,1 <n
    · nums1 [i] nums2 [j] nums3 [k] nums4 [1] ==0
'''

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int: