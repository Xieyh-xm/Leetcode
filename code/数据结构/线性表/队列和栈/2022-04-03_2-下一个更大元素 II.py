'''下一个更大元素 II

给定一个循环数组 nums ，返回 nums 中每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出-1。
* 多了个循环！

输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
'''

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stack = [0]   # 保存序号
        # 循环两遍
        for i in range(2*n):
            idx = i % n
            while len(stack) != 0 and nums[idx] > nums[stack[-1]]:
                ans[stack[-1]] = nums[idx]
                stack.pop()
            stack.append(idx)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements([1, 2, 1]))
