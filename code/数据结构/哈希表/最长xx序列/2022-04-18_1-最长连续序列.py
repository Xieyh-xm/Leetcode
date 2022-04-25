'''
最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为O(n) 的算法解决此问题。

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''

from typing import List

'''核心：用哈希表存储每个值作为端点时对应连续区间的长度，遍历一遍列表，不断更新表与maxLength
    用哈希表存储每个端点值对应连续区间的长度
    若数已在哈希表中：跳过不做处理
    若是新数加入：
        取出其左右相邻数已有的连续区间长度 left 和 right
        计算当前数的区间长度为：cur_length = left + right + 1
        根据 cur_length 更新最大长度 max_length 的值
        更新区间两端点的长度值'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = dict()
        maxLength = 0
        for i, val in enumerate(nums):
            if val not in hashMap:
                left = hashMap.get(val - 1, 0)
                right = hashMap.get(val + 1, 0)
                length = 1 + left + right
                hashMap[val - left] = length
                hashMap[val + right] = length
                hashMap[val] = length
                maxLength = max(maxLength, length)
        return maxLength


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]))
