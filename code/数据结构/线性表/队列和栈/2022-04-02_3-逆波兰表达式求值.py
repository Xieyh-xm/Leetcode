'''
逆波兰表达式求值

根据逆波兰表示法，求表达式的值。
有效的算符包括+、一、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
注意两个整数之间的除法只保留整数部分。
可以保证给定的逆波兰表达式总是有效的。
换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=None
        cache=[]
        for i,val in enumerate(tokens):
            if val=="+" or val=="-" or val =="*" or val=="/":
                if val=="+":
                    ans=cache[-2]+cache[-1]
                elif val=="-":
                    ans=cache[-2]-cache[-1]
                elif val =="*":
                    ans=cache[-2]*cache[-1]
                elif val=="/":
                    ans=int(cache[-2]/cache[-1])
                cache.pop()
                cache.pop()
                cache.append(ans)
            else:
                cache.append(int(val))
        return cache[-1]
    
if __name__=='__main__':
    s=Solution()
    print(s.evalRPN(["2","1","+","3","*"]))