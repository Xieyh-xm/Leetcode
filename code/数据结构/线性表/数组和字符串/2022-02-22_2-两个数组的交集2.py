'''
两个数组的交集2
给你两个整数数组 nums1 和 nums2，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
可以不考虑输出结果的顺序。
---------------------------------------------
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
---------------------------------------------
======> 进阶：
·如果给定的数组已经排好序呢？你将如何优化你的算法？
·如果 nums1 的大小比 nums2 小，哪种方法更优？
·如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''
import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''方法一：哈希表'''
        # trick 只对最小数组进行哈希映射
        # if len(nums1) > len(nums2):
        #     return self.intersect(nums2, nums1)
        # target = []
        # m = collections.Counter()
        # # 1. 建立哈希映射
        # for num in nums1:
        #     m[num] += 1
        # # 2. 遍历检查数字
        # for num in nums2:
        #     if m[num] != 0:
        #         target.append(num)
        #         m[num] -= 1
        # return target
        '''方法二：排序+双指针'''
        target = []
        # 1. 先进行排序
        nums1.sort()
        nums2.sort()
        # 2. 双指针移动
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                target.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return target
