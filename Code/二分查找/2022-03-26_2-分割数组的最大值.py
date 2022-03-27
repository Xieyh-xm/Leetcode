'''
分割数组的最大值
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。

输入：nums = [7,2,5,10,8], m = 2
输出：18
'''


from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        -------- 二分查找 + 贪心 --------
        选定一个值 xx，线性地验证是否存在一种分割方案，满足其最大分割子数组和不超过 xx。
           策略如下：
                贪心地模拟分割的过程，从前到后遍历数组.
                用 sum 表示当前分割子数组的和，cnt 表示已经分割出的子数组的数量（包括当前子数组）.
                每当 sum 加上当前值超过了 x，我们就把当前取的值作为新的一段分割子数组的开头，并将 cnt 加 1。
                遍历结束后验证是否 cnt 不超过 m。
            这样我们可以用二分查找来解决。二分的上界为数组 nums 中所有元素的和，下界为数组 nums 中所有元素的最大值。
            通过二分查找，我们可以得到最小的最大分割子数组和，这样就可以得到最终的答案了。
        '''

        # 贪心地模拟分割的过程，从前到后遍历数组.
        def stimulateDivide(target:int)->bool:
            sum,count=0,1
            for i,val in enumerate(nums):
                if sum+val>target:
                    sum=val
                    count+=1
                else:
                    sum+=val
            return count<=m

        # 二分查找
        lo,hi=max(nums),sum(nums)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if stimulateDivide(mid):
                hi=mid
            else:
                lo=mid+1
        return lo

if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8], 2))
