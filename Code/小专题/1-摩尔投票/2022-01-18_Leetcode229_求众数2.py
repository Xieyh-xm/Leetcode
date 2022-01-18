'''229. 求众数 II
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_1 = 0
        count_2 = 0
        candidate_1 = None
        candidate_2 = None
        # 1. 对抗阶段
        for num in nums:
            # A阵营或B阵营已经没有士兵，将当前遍历到的士兵作为潜在士兵
            if count_1 == 0 and num != candidate_2:
                candidate_1 = num
            elif count_2 == 0 and num != candidate_1:
                candidate_2 = num
            # 属于A或B
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
            else:  # 既不属于A也不属于B
                count_1 = count_1 - 1
                count_2 = count_2 - 1
        # 2. 计数阶段，判断A和B是否超过1/3
        check_cnt_1 = 0
        check_cnt_2 = 0
        for num in nums:
            if num == candidate_1:
                check_cnt_1 += 1
            elif num == candidate_2:
                check_cnt_2 += 1
        list = []
        if check_cnt_1 > len(nums) / 3:
            list.append(candidate_1)
        if check_cnt_2 > len(nums) / 3:
            list.append(candidate_2)
        return list
