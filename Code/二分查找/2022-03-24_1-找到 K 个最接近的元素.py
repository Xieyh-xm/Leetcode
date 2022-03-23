'''
找到 K 个最接近的元素
给定一个排序好的数组 arr，两个整数 k 和 x，从数组中找到最靠近×（两数之差最小）的 k 个数。
返回的结果必须要是按升序排好的。整数 a 比整数 b 更接近 x 需要满足：
· a-x <b-x 或者
· |a-x|==|b-x| 且 a<b

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
'''

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]: