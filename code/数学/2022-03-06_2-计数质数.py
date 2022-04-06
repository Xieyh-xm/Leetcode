'''
计数质数
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
---------------------------------------------
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
---------------------------------------------
'''
from math import ceil

class Solution:
    def countPrimes(self, n: int) -> int:
        '''方法一：埃氏筛'''
        cnt = 0
        isPrimes = [1] * n  # 1表示质数
        for i in range(2, len(isPrimes)):
            if isPrimes[i]:  # 是质数
                cnt += 1
                for j in range(i * i, n, i):
                    isPrimes[j] = 0
        return cnt

        '''方法二：试除法，会超时'''
        # if n <= 2:
        #     return 0
        # if n == 3:
        #     return 1
        # primes = [2]
        # for i in range(3, n, 2):
        #     flag = False
        #     sqrt = int(pow(i, 0.5))
        #     for prime in primes[1:]:
        #         if prime > sqrt:
        #             break
        #         if i % prime == 0:
        #             flag = True
        #             break
        #     if flag == False:
        #         primes.append(i)
        # return len(primes)
