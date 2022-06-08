'''根据身高重建队列'''

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: 1000 * x[1] + 0.0001 * x[0])
        ans = []
        for idx, val in enumerate(people):
            if val[1] == 0:
                ans.append(val)
                continue
            cnt, idx = 0, 0
            while cnt < val[1]:
                if ans[idx][0] >= val[0]:
                    cnt += 1
                idx += 1
            while idx < len(ans) and ans[idx][0] < val[0]:
                idx += 1
            ans.insert(idx, val)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
