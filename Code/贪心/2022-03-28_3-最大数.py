'''
最大数
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

输入：nums = [10,2]
输出："210"

输入：nums = [3,30,34,5,9]
输出："9534330"
'''

from typing import List

'''
可以根据「结果」来决定 aa 和 bb 的排序关系：
如果拼接结果 abab 要比 baba 好，那么我们会认为 aa 应该放在 bb 前面。'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 取出第一个数字
        def swap(a,b):
            return b,a
        def isBigger(num,target)->bool:
            tmp_1=str(num)+str(target)
            tmp_2=str(target)+str(num)
            if int(tmp_1)>=int(tmp_2):
                return True
            else:
                return False
        ans=""
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if not isBigger(nums[j],nums[j+1]):
                    nums[j],nums[j+1]=swap(nums[j],nums[j+1])
        for i in range(len(nums)):
            # 排除[0,0,0]的情况
            if len(ans)>0 and int(ans)==0 and nums[i]==0:
                continue
            ans+=str(nums[i])
        return ans

'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'

作者：AC_OIer
链接：https://leetcode-cn.com/problems/largest-number/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-vn86e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

if __name__=='__main__':
    s=Solution()
    print(s.largestNumber([0,0,0]))