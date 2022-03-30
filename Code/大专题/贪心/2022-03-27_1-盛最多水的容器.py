'''
盛最多水的容器
给定一个长度为 n 的整数数组 1 height。有 n 条垂线，第 i 条线的两个端点是（i,0) 和（i, height [i]）。
找出其中的两条线，使得它们与ⅹ轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。
说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''----- 双指针 -----'''
        def calArea(l:int,r:int)->int:
            return (r-l)*min(height[l],height[r])
        
        lo,hi=0,len(height)-1
        ans=0
        while lo<hi:
            cur=calArea(lo,hi)
            ans=max(ans,cur)
            # 即无论我们怎么移动右指针，得到的容器的容量都小于移动前容器的容量。
            # 也就是说，这个左指针对应的数不会作为容器的边界了
            if height[lo]<height[hi]:
                lo+=1
            else:
                hi-=1
        return ans

if __name__=='__main__':
    s=Solution()
    print(s.maxArea([2,3,4,5,18,17,6]))