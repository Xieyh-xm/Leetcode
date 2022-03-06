'''
合并两个有序数组
给你两个按非递减顺序排列的整数数组 nums1 和 nums2, 另有两个整数 m 和 n，分别表示 nums1 和 nums2 中的元素数目。
请你合并 nums2 到 nums1 中，使合并后的数组同样按非递减顺序排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m+n，其中前 m
个元素表示应合并的元素，后 n 个元素为 0，应忽略。nums2 的长度为 n。

---------------------------------------------
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
---------------------------------------------
'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1, index_2 = 0, 0
        count = 0  # 记录nums有几个数排好序了
        while count <= m and index_2 < n:
            if nums1[index_1] <= nums2[index_2]:
                index_1 += 1
                count += 1
            else:
                # 1. num1元素向后移动
                for i in range(m + index_2 - index_1 - 1, -1, -1):
                    nums1[index_1 + i + 1] = nums1[index_1 + i]
                # 2. 插入元素
                nums1[index_1] = nums2[index_2]
                # 3. 移动index
                index_1 += 1
                index_2 += 1

        if index_2 < n:
            for i in range(n - index_2):
                nums1[index_2 + count + i] = nums2[index_2 + i]
        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    solution.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
