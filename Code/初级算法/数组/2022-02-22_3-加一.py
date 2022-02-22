'''
加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位，数组中每个元素只存储单个数字。你可以假设除了整数 0 之外，这个整数不会以零开头。
---------------------------------------------
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

输入：digits = [9,9,9]
输出：[1,0,0,0]
---------------------------------------------
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        sum = 0
        for i in range(len(digits)):
            sum = sum + digits[-i - 1] * pow(10, i)
        sum += 1
        length = len(digits)
        if sum >= pow(10, len(digits)):
            length += 1
        for i in range(length):
            temp = int(sum / pow(10, length - i - 1))
            sum = sum - temp * pow(10, length - i - 1)
            result.append(temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9, 9, 9]))
