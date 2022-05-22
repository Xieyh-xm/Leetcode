'''数组中和为 0 的三个数'''
from typing import List

'''哈希表：超时且占用空间很大'''
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         hashMap = dict()
#         ans = []
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] in hashMap:
#                     hashMap[nums[i] + nums[j]].append([i, j])
#                 else:
#                     hashMap[nums[i] + nums[j]] = [[i, j]]
#         for i, val in enumerate(nums):
#             if nums[i] == nums[i - 1]:
#                 continue
#             if -val in hashMap:
#                 for j in range(len(hashMap[-val])):
#                     if i not in hashMap[-val][j] and nums[i] <= nums[hashMap[-val][j][0]]:
#                         tmp = [nums[i]]
#                         for idx in hashMap[-val][j]:
#                             tmp.append(nums[idx])
#                         if tmp not in ans:
#                             ans.append(tmp)
#         return ans

'''双指针'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
