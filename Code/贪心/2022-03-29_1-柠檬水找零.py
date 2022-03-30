'''
柠檬水找零
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bi11s 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
给你一个整数数组 bi11s，其中 bi11s[i]是第i位顾客付的账。如果你能给每位顾客正确找零，返回 true，否则返回 false

输入：bills = [5,5,5,10,20]
输出：true
'''


from typing import List

'''哈希表 + 贪心算法'''
'''把最不常用的找出去（面额大的），因为两个5元比一个10元更加灵活，适用的场景更多'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coin = {5: 0, 10: 0, 20: 0}
        for i, val in enumerate(bills):
            coin[val] += 1
            if val == 10:
                coin[5] -= 1
            elif val == 20:
                if coin[10] > 0:
                    coin[10] -= 1
                    coin[5] -= 1
                else:
                    coin[5] -= 3
            if coin[5] < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.lemonadeChange([5, 5, 5, 10, 20]))
