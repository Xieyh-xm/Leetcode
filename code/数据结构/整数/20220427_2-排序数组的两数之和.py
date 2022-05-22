'''排序数组的两数之和'''
from typing import List

'''哈希表'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, val in enumerate(numbers):
            if val in hashMap:
                return [hashMap[val], i]
            else:
                hashMap[target - val] = i
        return []

'''双指针'''