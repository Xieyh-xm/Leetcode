'''下一个更大元素 III

给你一个正整数 n，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，
并且其值大于 n。如果不存在这样的正整数，则返回-1
注意，返回的整数应当是一个 32 位整数，如果存在满足题意的答案，但不是 32 位整数,同样返回-1

输入：n = 12
输出：21
'''


import sys


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = [n % 10]
        stack_tmp=[]
        n = int(n/10)
        while n != 0:
            # 取出最末的元素
            tmp = n % 10
            n=int(n/10)
            if tmp >= stack[-1]:
                stack.append(tmp)
            else:
                i=0
                while len(stack)!=0 and stack[-1]>tmp:
                    stack_tmp.append(stack.pop())
                n=n*10+stack_tmp.pop()
                for i in range(len(stack)):
                    n=n*10+stack[i]
                n=n*10+tmp
                while stack_tmp:
                    n=n*10+stack_tmp.pop()
                if n>2**31 - 1:
                    return -1
                return n
        return -1

if __name__=='__main__':
    s=Solution()
    print(s.nextGreaterElement(12321))
