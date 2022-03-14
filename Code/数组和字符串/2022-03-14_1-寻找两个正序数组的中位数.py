'''
寻找两个正序数组的中位数

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
算法的时间复杂度应该为 0 (1og (m+n））。

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''方法一：时间复杂度不达标'''
        index_num1, index_num2 = 0, 0
        array = []
        while index_num1 < len(nums1) and index_num2 < len(nums2):
            if nums1[index_num1] <= nums2[index_num2]:
                array.append(nums1[index_num1])
                index_num1 += 1
            else:
                array.append(nums2[index_num2])
                index_num2 += 1
        if index_num1 < len(nums1):
            array += nums1[index_num1:]
        else:
            array += nums2[index_num2:]

        if len(array) % 2 == 1:
            return array[len(array) // 2]
        else:
            return 0.5 * (array[len(array) // 2] + array[len(array) // 2 - 1])
        '''方法二：二分查找，累了算了'''



if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2, 3, 5, 6, 7, 8]))
