'''分割回文串'''
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret, path = [], []

        # 确认是否回文
        def check(sub_str: List) -> bool:
            if len(sub_str) == 0:
                return False
            left, right = 0, len(sub_str) - 1
            while left <= right:
                if sub_str[left] != sub_str[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtracking(startIdx) -> None:
            if startIdx >= len(s):
                ret.append(path[:])
                return
            for i in range(startIdx, len(s) + 1):
                if check(s[startIdx:i]):
                    path.append(s[startIdx:i])
                    backtracking(i)
                    path.pop()
                else:
                    continue
            return

        backtracking(0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition("aab"))
