'''
在排序数组中查找元素的第一个和最后一个位置

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
'''


import numbers
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        # 找左右边界
        l, r = 0, len(nums)
        idx_l, idx_r = 0, len(nums)
        # 右边界
        while l < r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                l = mid+1
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid
        if nums[l-1]==target:
            idx_r=l-1
        else:
            return [-1,-1]
        # 左边界
        l,r=0,idx_r
        while l < r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                r = mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid
        idx_l=r
        return [idx_l,idx_r]

if __name__=='__main__':
    s=Solution()
    print(s.searchRange([5,7,7,8,8,8,10],8))
