'''
加油站
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i]升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost [1] 升。
你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回-1。
如果存在解，则保证它是唯一的。

输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
'''

import sys
from typing import List

'''注意：先消耗，再加'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        min_sum=sys.maxsize
        min_index=0
        sum=0
        for i in range(n):
            # 假设第一个点的剩余油量是0
            sum+=gas[i]-cost[i] # 刚到第i站的剩余油量
            if sum<min_sum:
                min_sum=sum
                min_index=i
        if sum>=0:
            # 因为总（gas-cost）是大于等于0的，所以前面损失的gas我从最低点下一个点开始都会拿回来！
            return (min_index+1)%n
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([3,1,1], [1,2,2]))
