'''
找出第 k 小的距离对
给定一个整数数组，返回所有数对之间的第 k 个最小距离。
一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

输入：
nums = [1,3,1]
k = 1
输出：0 
'''

from typing import List
        
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        '''双指针'''
        def get_count(dis):
            cnt = l = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dis:
                    # 距离大了左指针要跟上
                    l += 1
                cnt += r - l    # 它和之前的数的距离小于mid的数量为r-l
            return cnt
        
        '''二分法'''
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            if get_count(mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__=='__main__':
    s=Solution()
    print(s.smallestDistancePair([1,3,1],2))