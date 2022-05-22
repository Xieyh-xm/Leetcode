'''只出现一次的数字
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        haspMap = dict()
        for i, val in enumerate(nums):
            if val in haspMap:
                haspMap[val] += 1
                if haspMap[val] == 3:
                    del haspMap[val]
            else:
                haspMap[val] = 1
        return list(haspMap.keys())[0]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 3, 2]))
