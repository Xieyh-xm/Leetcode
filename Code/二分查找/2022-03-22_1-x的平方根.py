'''
x 的平方根
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
由于返回类型是整数，结果只保留整数部分 ，小数部分将被舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

输入：x = 4
输出：2
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        idx_left,idx_right=0,x
        while idx_left<idx_right:
            mid=idx_left+(idx_right-idx_left)//2
            # 这里可以考虑换成除法，避免整数溢出
            if mid**2>x:
                idx_right=mid-1
            elif (mid+1)**2<=x:
                idx_left=mid+1
            else:
                return mid
        return idx_left

if __name__=='__main__':
    solution=Solution()
    print(solution.mySqrt(1))