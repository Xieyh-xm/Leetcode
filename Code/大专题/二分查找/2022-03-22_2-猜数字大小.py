'''
猜数字大小

猜数字游戏的规则如下：
·每轮游戏，我都会从 1 到 n 随机选择一个数字。请你猜选出的是哪个数字。
·如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess (int num）来获取猜测结果，返回值一共有 3 种可能的情况（-1,1 或 0)：

-1：我选出的数字比你猜的数字小 pick <num
1: 我选出的数字比你猜的数字大 pick> num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick==num

返回我选出的数字。

输入：n = 10, pick = 6
输出：6
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
from re import X
from xml.dom import minidom


def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        idx_left,idx_right=0,n
        while idx_left<idx_right:
            mid=idx_left+(idx_right-idx_left)//2
            flag=guess(mid)
            if flag==-1:
                idx_right=mid-1
            elif flag==1:
                idx_left=mid+1
            else:
                return mid
        return idx_left