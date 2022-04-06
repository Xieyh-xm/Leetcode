'''
存在重复元素 II
给你一个整数数组 nums 和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，满足 nums [i] ==nums [j]且 abs (i- j) <=k。
如果存在，返回 true；否则，返回 false。

输入：nums = [1,2,3,1], k = 3
输出：true
'''

from ast import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # haspMap存储数字出现的位置（出现过检查+更新，未出现过新增）
        dict={}
        for i,val in enumerate(nums):
            if val in dict and i-dict[val] <= k:
                return True
            dict[val]=i
        return False