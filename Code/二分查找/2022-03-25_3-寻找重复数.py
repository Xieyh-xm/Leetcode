'''
寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

输入：nums = [1,3,4,2,2]
输出：2
'''

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''快慢指针'''
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        l,r=0,slow
        while l!=r:
            l=nums[l]
            r=nums[r]
        return l
            


if __name__=='__main__':
    s=Solution()
    print(s.findDuplicate([1,3,4,2,2]))