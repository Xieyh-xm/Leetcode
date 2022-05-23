'''分发饼干'''

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ret = 0
        idx = 0
        for i, val in enumerate(g):
            # 没有饼干了
            if i >= len(s):
                return ret
            while g[i] > s[idx]:
                idx += 1
                if idx >= len(s):
                    return ret
            ret += 1
            idx += 1
            if idx >= len(s):
                return ret
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
