'''有序数组的平方
给你一个按非递减顺序排序的整数数组 nus，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
'''

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 先找到第一个大于0的
        idx=-1
        for i,val in enumerate(nums):
            if val>=0 or i==len(nums)-1:
                idx=i
                break
        # 双指针
        ans=[]
        lo,hi=idx-1,idx
        while lo>=0 or hi<len(nums):
            if hi>=len(nums):
                ans.append(nums[lo]**2)
                lo-=1
                continue
            elif lo<0:
                ans.append(nums[hi]**2)
                hi+=1
                continue            
            if abs(nums[lo])<=abs(nums[hi]):
                ans.append(nums[lo]**2)
                lo-=1
            elif abs(nums[lo])>=abs(nums[hi]):
                ans.append(nums[hi]**2)
                hi+=1
        return ans
    
if __name__=='__main__':
    s=Solution()
    print(s.sortedSquares([-7,-3,2,3,11]))
    

