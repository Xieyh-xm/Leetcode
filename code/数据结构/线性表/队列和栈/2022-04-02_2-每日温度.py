'''
每日温度

给定一个整数数组 temperatures，表示每天的温度，返回一个数组answer，其中 answer[i]是指在第 i 天之后，才会有更高的温度。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
'''

from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q_idx=[0]
        for i in range(1,len(temperatures)):
            while len(q_idx)!=0 and temperatures[i]>temperatures[q_idx[-1]]:
                idx=q_idx.pop()
                temperatures[idx]=i-idx
            q_idx.append(i)
        while len(q_idx)!=0:
            temperatures[q_idx.pop()]=0
        return temperatures
    
if __name__=='__main__':
    s=Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))