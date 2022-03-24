'''
有效的完全平方数
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 true，否则返回 fa1lse。
进阶：不要使用任何内置的库函数，如 sgrt。

输入：num = 14
输出：false
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo <= hi:
            mid = lo+(hi-lo)//2
            if num / mid == mid:
                return True
            elif num/mid < mid:
                hi = mid-1
            elif num/mid > mid:
                lo = mid+1
        return False

if __name__=='__main__':
    s=Solution()
    print(s.isPerfectSquare(14))