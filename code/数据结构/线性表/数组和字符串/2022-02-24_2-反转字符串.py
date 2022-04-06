'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用O(1)的额外空间解决这一问题。
---------------------------------------------
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
---------------------------------------------
'''
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 'str' object does not support item assignment 有问题
        for i in range(int(len(s) / 2)):
            temp = s[-i - 1]
            s[-i - 1] = s[i]
            s[i] = temp

        '''还可以试一下双指针...'''


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseString("abc"))
