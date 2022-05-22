'''复原 IP 地址'''

from typing import List


# 本质分割问题，和组合问题类似
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret, path = [], []

        def check(sub_str):
            if len(sub_str) == 0:
                return False
            return (sub_str[0] != '0' and 0 <= int(sub_str) <= 255) or sub_str == '0'

        def backtracking(startIdx):
            if startIdx >= len(s):
                if len(path) != 4:
                    return
                ret.append(".".join(path[:]))
                return
            for i in range(startIdx, len(s) + 1):
                if check(s[startIdx:i]):
                    path.append(s[startIdx:i])
                    backtracking(i)
                    path.pop()
            return

        backtracking(0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses("101023"))
