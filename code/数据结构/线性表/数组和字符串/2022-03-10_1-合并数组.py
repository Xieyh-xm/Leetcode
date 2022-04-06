'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
---------------------------------------------
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
---------------------------------------------
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # def swap(list1, list2):
        #     return list2, list1
        # 1. 左端点排序
        # -----> 注意：冒泡排序很耗时！！！ <-----
        # for i in range(len(intervals) - 1):
        #     for j in range(len(intervals) - i - 1):
        #         if intervals[j][0] > intervals[j + 1][0]:
        #             intervals[j], intervals[j + 1] = swap(intervals[j], intervals[j + 1])
        intervals.sort(key=lambda x: x[0])
        # 2. 遍历合并数组
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                if intervals[i][1] > ans[-1][1]:
                    ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18], [1, 10000]]))
