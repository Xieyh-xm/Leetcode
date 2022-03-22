'''
二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回-1。

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
'''

from tkinter import S
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.biSearch(nums,0,len(nums)-1,target)

    def biSearch(self,nums:List[int],idx_left:int,idx_right:int,target):
        if idx_right<=idx_left:
            if target==nums[idx_right]:
                return idx_right
            else:
                return -1
        mid=(idx_left+idx_right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.biSearch(nums,idx_left,mid-1,target)
        else:
            return self.biSearch(nums,mid+1,idx_right,target)
        
if __name__=='__main__':
    solution=Solution()
    print(solution.search([-1,0,3,5,9,12],2))