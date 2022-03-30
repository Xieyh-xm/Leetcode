'''
分发糖果
N 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
· 每个孩子至少分配到 1 个糖果。
· 相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的最少糖果数目。

输入：ratings = [1,2,2]
输出：4
'''

from typing import List

'''
贪心策略为：在每次遍历中，只考虑并更新相邻一侧的大小结果

设学生 AA 和学生 BB 左右相邻，AA 在 BB 左边:
    左规则：当 ratingsB> ratingsA 时，B 的糖比 A 的糖数量多。 
    右规则：当 ratingsA> ratingsB 时，A 的糖比 B 的糖数量多。
相邻的学生中，评分高的学生必须获得更多的糖果 等价于 所有学生满足左规则且满足右规则。
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = 0
        n = len(ratings)
        # 给每个人分一个糖果
        left, right = [1]*n, [1]*n
        # 左遍历
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
        # 右遍历
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
        # 取max
        for i in range(n):
            ans += max(left[i], right[i])
        return ans

        '''
        思路：
        1. 找到rating最低的那个孩子
        2. 双指针分发向外
        行不通！！！！！
        反例：[1,3,2,2,1]
        '''
        # idx=ratings.index(min(ratings))
        # lo,hi=idx-1,idx+1
        # lo_suger_last,hi_suger_last=1,1
        # ans=1
        # while lo>=0 or hi<len(ratings):
        #     # 处理左
        #     if lo>=0:
        #         if ratings[lo]>ratings[lo+1]:
        #             lo_suger_last+=1
        #         else:
        #             lo_suger_last=max(lo_suger_last-1,1)
        #         ans+=lo_suger_last
        #         lo-=1
        #     # 处理右
        #     if hi<len(ratings):
        #         if ratings[hi]>ratings[hi-1]:
        #             hi_suger_last+=1
        #         else:
        #             hi_suger_last=max(hi_suger_last-1,1)
        #         ans+=hi_suger_last
        #         hi+=1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1,3,4,5,2]))
