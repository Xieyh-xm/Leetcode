'''
寻找旋转排序数组中的最小值 II

输入：nums = [2,2,2,0,1]
输出：0
'''


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            # print(nums[mid])
            if nums[mid]>nums[hi]:
                lo=mid+1
            elif nums[mid]<nums[hi]:
                hi=mid
            elif nums[mid]==nums[hi]:
                # 无论 nums[right] 是不是最小值，剩下区间中都有一个 nums[mid] 作为它的替代值
                hi-=1
        return nums[lo]

if __name__=='__main__':
    s=Solution()
    print(s.findMin([2,2,2,0,1]))
