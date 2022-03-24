'''
Pow(x, n)

输入：x = 2.00000, n = -2
输出：0.25000
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 负数全转化为正数计算
        if n < 0:
            return self.Pow(1/x, -n)
        return self.Pow(x, n)

    def Pow(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 1:
            return x*self.myPow(x, n//2)**2
        else:
            return self.myPow(x, n//2)**2

if __name__=='__main__':
    s=Solution()
    print(s.myPow(4,3))