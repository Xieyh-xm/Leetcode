'''
移除元素
给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 0 (1) 额外空间并原地修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

---------------------------------------------
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
---------------------------------------------
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''快慢指针'''
        index_right = len(nums) - 1
        count = 0
        for index_left in range(len(nums)):
            if nums[index_left] == val:
                count += 1
                while nums[index_right] == val and index_right >= 0:
                    index_right -= 1
                nums[index_left] = nums[index_right]
                index_right -= 1
        print(nums)
        return len(nums) - count


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([1], 1))
