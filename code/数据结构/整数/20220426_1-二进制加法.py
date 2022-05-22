'''二进制加法
    类似于实现一个加法器
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)
        ans = ""
        carry_flag = 0
        for i in range(len(a)):
            idx = -i - 1
            if i < len(b):
                if a[idx] != b[idx]:
                    tmp = 1
                elif a[idx] == '1':
                    tmp = 2
                else:
                    tmp = 0
            else:
                tmp = int(a[idx])
            value = (tmp + carry_flag) % 2
            carry_flag = (tmp + carry_flag) // 2
            ans = str(value) + ans
        if carry_flag == 1:
            return '1' + ans
        return ans
