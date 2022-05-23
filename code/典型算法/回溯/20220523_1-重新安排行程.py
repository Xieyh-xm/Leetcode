'''重新安排行程'''

from typing import List


# 回溯法：类似排列
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ret, path = [], []
        used = [False for k in range(len(tickets))]

        def backtracking() -> None:
            if len(path) == len(tickets) + 1:
                ret.append(path[:])
                # print(ret)
                return
            for i in range(len(tickets)):
                if used[i]:
                    continue
                if len(path) == 0:
                    if tickets[i][0] == 'JFK':
                        used[i] = True
                        path.append(tickets[i][0])
                        path.append(tickets[i][1])
                        backtracking()
                        path.pop()
                        path.pop()
                        used[i] = False
                        if len(ret) > 0:
                            break
                elif path[-1] == tickets[i][0]:
                    used[i] = True
                    path.append(tickets[i][1])
                    backtracking()
                    used[i] = False
                    path.pop()
                    if len(ret) > 0:
                        break
            return

        tickets = sorted(tickets)
        # print(tickets)
        backtracking()
        return ret[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
