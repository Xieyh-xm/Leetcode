'''
寻找旋转排序数组中的最小值
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次旋转后，得到输入数组。例如，原数组 nums= [0,1,2,4,5,6,7]

在变化后可能得到：
若旋转 4 次，则可以得到[4,5,6,7,0,1,2]
若旋转 7 次，则可以得到[0,1,2,4,5,6,7]
注意，数组【a [0], a [1], a [2],, a [n-1】】旋转-次的结果为数组【a [n-1], a [0], a [1], a [2],, a [n-2]。

给你一个元素值互不相同的数组 nus，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的最小元素。
你必须设计一个时间复杂度为 0 (1ogn）的算法解决此问题。

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.bisection(nums, 0, len(nums) - 1)

    def bisection(self, nums, left: int, right: int) -> int:
        if abs(left - right) <= 1:
            return min(nums[left], nums[right], nums[0])
        mid = (left + right) // 2
        if nums[mid] > nums[left]:
            return self.bisection(nums, mid, right)
        else:
            return self.bisection(nums, left, mid)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin([11, 13, 15, 17]))
