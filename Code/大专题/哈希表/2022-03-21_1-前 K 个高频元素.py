'''
前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
你可以按 任意顺序 返回答案。

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
'''

import collections
from multiprocessing.connection import answer_challenge
from typing import List


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # 维持一个前k高元素的list
#         ans = []
#         freq_min = 0
#         m = collections.Counter()
#         def sortFreq(idx):
#             for i in range(idx, 0, -1):
#                 if m[ans[i]] <= m[ans[i-1]]:
#                     break
#                 else:
#                     tmp = ans[i]
#                     ans[i] = ans[i-1]
#                     ans[i-1] = tmp

#         for key in nums:
#             m[key] += 1
#             if key not in ans:
#                 if len(ans) < k:
#                     ans.append(key)
#                 elif m[key] > freq_min:
#                     ans[-1] = key
#                 sortFreq(len(ans)-1)
#             else:
#                 idx=len(ans)-1
#                 while ans[idx]!=key:
#                     idx-=1
#                 sortFreq(idx)
#             freq_min = m[ans[-1]]
#         return ans

'''上面的方法太慢了，可以计数完再维护最小堆'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=collections.Counter(nums)
        ans=[]
        freq_min = 0
        def sortFreq():
            for i in range(len(ans)-1, 0, -1):
                if m[ans[i]] <= m[ans[i-1]]:
                    break
                else:
                    tmp = ans[i]
                    ans[i] = ans[i-1]
                    ans[i-1] = tmp
        for key,val in m.items():
            if len(ans)<k:
                ans.append(key)
                sortFreq()
                freq_min=m[ans[-1]]
            elif val>freq_min:
                ans[-1]=key
                sortFreq()
                freq_min=m[ans[-1]]
        return ans

if __name__=='__main__':
    solution=Solution()
    print(solution.topKFrequent([1,3,3,2,2,3],2))