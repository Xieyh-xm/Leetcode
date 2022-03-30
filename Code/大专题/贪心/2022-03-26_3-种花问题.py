'''
种花问题
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

输入：flowerbed = [1,0,0,0,1], n =1
输出：true
'''


from curses.ascii import SO
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        if len(flowerbed) == 1:
            return n == 0 or (n == 1 and flowerbed[0] == 0)
        for i, val in enumerate(flowerbed):
            if val == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        cnt += 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        cnt += 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        cnt += 1
            if cnt >= n:
                return True
        return False

if __name__=='__main__':
    s=Solution()
    print(s.canPlaceFlowers([1,0,0,0,1],6))