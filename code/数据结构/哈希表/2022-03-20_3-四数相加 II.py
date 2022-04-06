'''
四数相加 II
给你四个整数数组 nums1、nums2、nums3 和 nums4, 数组长度都是 n.
请你计算有多少个元组（i, j, k,1) 能满足：
    · 0 <=i, j, k,1 <n
    · nums1 [i] nums2 [j] nums3 [k] nums4 [1] ==0

输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
--- 两个元组如下 ---
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
'''

import collections
from itertools import count
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        '''方法一：分组表 + 哈希表'''
        m = collections.Counter()
        for val_1 in nums1:
            for val_2 in nums2:
                m[val_1+val_2] += 1
        count = 0
        for val_3 in nums3:
            for val_4 in nums4:
                if -(val_3+val_4) in m:
                    count += m[-(val_3+val_4)]
        return count
