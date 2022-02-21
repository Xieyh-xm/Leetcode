from typing import List


# bug原因：索引初始化不对
class Solution:
    ''' 直觉做法 '''
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     cnt = 1
    #     # 1. 置None
    #     cur_num = nums[0]
    #     for i in range(1, len(nums)):
    #         next_num = nums[i]
    #         if cur_num != next_num:
    #             cnt = cnt + 1
    #             cur_num = next_num
    #         else:
    #             nums[i] = None
    #     # 2. 调整位置
    #     index = 1
    #     for i in range(1, len(nums)):
    #         if nums[i] is not None:
    #             nums[index] = nums[i]
    #             index = index + 1
    #     return cnt, nums

    ''' 双指针做法 '''

    def removeDuplicates(self, nums: List[int]) -> int:
        '''思路：使用left和right两个指针'''
        left = 0
        # i就是右指针
        for i in range(len(nums)):
            if nums[left] != nums[i]:
                left += 1
                nums[left] = nums[i]
        return len(nums[0:left + 1]), nums


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    cnt, nums = solution.removeDuplicates(nums)
    print("cnt = " + str(cnt) + " | " + str(nums))
