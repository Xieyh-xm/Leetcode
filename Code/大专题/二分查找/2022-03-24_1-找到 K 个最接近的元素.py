'''
找到 K 个最接近的元素
给定一个排序好的数组 arr，两个整数 k 和 x，从数组中找到最靠近×（两数之差最小）的 k 个数。
返回的结果必须要是按升序排好的。整数 a 比整数 b 更接近 x 需要满足：
· a-x <b-x 或者
· |a-x|==|b-x| 且 a<b

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
'''

from tkinter import N
from typing import List

'''思路：二分法 + 双指针'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 1. 先找到最接近的元素
        lo,hi=0,len(arr)-1
        while lo<hi:
            mid =lo+(hi-lo)//2
            if arr[mid]==x:
                lo,hi=mid,mid
            elif arr[mid]>x:
                hi=mid-1
            elif arr[mid]<x:
                lo=mid+1
        
        if arr[lo]>x and lo-1>=0:
            if abs(arr[lo-1]-x)<=abs(arr[lo]-x):
                lo,hi=lo-1,hi-1
        if arr[lo]<x and lo+1<len(arr):
            if abs(arr[lo+1]-x)<abs(arr[lo]-x):
                lo,hi=lo+1,hi+1

        # if lo==0:
        #     return arr[lo:lo+k]
        # else:
        #     if abs(x-arr[lo])>=abs(x-arr[lo-1]):
        #         lo,hi=lo-1,lo-1
        # 2. 双指针
        while hi-lo<k-1:
            if lo-1>=0 and hi+1<=len(arr)-1:
                if abs(x-arr[lo-1])<=abs(x-arr[hi+1]):
                    lo-=1
                else:
                    hi+=1
            elif lo-1<0:
                hi+=k-(hi-lo+1)
            elif hi+1>=len(arr):
                lo-=k-(hi-lo+1)
        return arr[lo:hi+1]

if __name__=='__main__':
    s=Solution()
    print(s.findClosestElements([1,3],1,2))  