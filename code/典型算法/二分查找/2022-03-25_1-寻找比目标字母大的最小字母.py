'''
寻找比目标字母大的最小字母
给你一个排序后的字符列表 letters，列表中只包含小写英文字母。另给出一个目标字母 target，
请你寻找在这一有序列表里比目标字母大的最小字母。在比较时，字母是依序循环出现的。

举个例子：
· 如果目标字母 target='z'并且字符列表为 letters=['a', 'b']，则答案返回'a'

输入: letters = ["c","f","j"], target = "d"
输出: "f"
'''
import bisect
from typing import List

'''找最小值？'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

if __name__=='__main__':
    s=Solution()
    print(s.nextGreatestLetter(["e","e","e","k","q","q","q","v","v","y"],"a"))