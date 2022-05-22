'''前 n 个数字二进制中 1 的个数'''
from typing import List
import math

'''
如果正整数 i 是一个偶数，那么 i 相当于将 i/2 左移一位的结果，因此偶数 i 和 i/2 的二进制形式 1 的个数是一样的 
如果 i 是奇数，那么 i 相当于将 i/2 左移一位之后再将最右边的位设为 1 的结果，因此奇数 i 比 i/2 的二进制形式 1 的个数多 1 个'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(num):
            if num // 2 == 0:
                return [0, 1]
            tmp = helper(num // 2)
            return tmp + [i + 1 for i in tmp]

        if n == 0:
            return [0]
        num = pow(2, int(math.log2(n)) + 1)
        ans = helper(num)
        return ans[0:n + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(0))
