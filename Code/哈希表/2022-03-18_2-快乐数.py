'''
快乐数
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：
· 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
· 然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。·如果这个过程结果为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true；不是，则返回 false。
'''

from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        def divideNum(num: int) -> List[int]:
            temp = []
            while num != 0:
                temp.append(num % 10)
                num = num//10
            return temp

        def sumOfSquares(l: list) -> int:
            sum = 0
            for i, val in enumerate(l):
                sum = sum+pow(int(val), 2)
            return sum
        # ---------------------------------
        m=set()
        while n != 1:
            l = divideNum(n)
            n = sumOfSquares(l)
            if n in m :
                return False
            m.add(n)
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(2))
