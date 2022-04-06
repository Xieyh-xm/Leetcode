'''
下一个更大元素 I

Nums1中数字x的下一个更大元素是指 x 在 nums2 中对应位置右侧的第一个比x大的元素。
给你两个没有重复元素的数组 nums1 和 nums2, 下标从 0 开始计数，其中 nums1 是 nums2 的子集。
对于每个 0<=i<nums1.Length，找出满足 nums1[i]==nums2[j] 的下标 j，并且在nums2 确定 nums2[j] 的下一个更大元素。
如果不存在下一个更大元素，那么本次查询的答案是-1
返回一个长度为 nums1. Length 的数组 ans 作为答案，满足 ans[i] 是如上所述的下一个更大元素

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
'''


from typing import List

'''
第 1 个子问题：如何更高效地计算 nums2 中每个元素右边的第一个更大的值；(单调栈)
第 2 个子问题：如何存储第 1 个子问题的结果。（哈希表）
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap={}
        stack=[0]
        for i in range(1,len(nums2)):
            while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                hashMap[nums2[stack[-1]]]=nums2[i]
                stack.pop()
            stack.append(i)
        
        for i in range(len(nums1)):
            if nums1[i] in hashMap:
                nums1[i]=hashMap[nums1[i]]
            else:
                nums1[i]=-1
        return nums1

if __name__=='__main__':
    s=Solution()
    print(s.nextGreaterElement([4,1,2],[1,3,4,2]))