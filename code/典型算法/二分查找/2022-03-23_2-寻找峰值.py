'''
寻找峰值
峰值元素是指其值严格大于左右相邻值的元素。
数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2
'''

from typing import List

'''上坡必有顶'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l <= r:
            mid = l+(r-l)//2
            if mid+1==len(nums) and nums[mid-1]<nums[mid]:
                return r-1
            if mid-1==-1:
                return l
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] > nums[mid]:
                # select left region
                r = mid
            elif nums[mid] < nums[mid+1]:
                # select right region
                l = mid+1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([2,1]))
