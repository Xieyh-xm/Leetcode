'''
回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。

输入：x = 121
输出：true
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        lo,hi=0,len(num)-1
        while lo<=hi:
            if num[lo]!=num[hi]:
                return False
            lo+=1
            hi-=1
        return True
    
'''可以考虑反转一半'''

if __name__=='__main__':
    s=Solution()
    print(s.isPalindrome(12231))
