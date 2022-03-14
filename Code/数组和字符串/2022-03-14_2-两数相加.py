'''
两数相加
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def countNum(self, node):
        count = 0
        i = 0
        while node != None:
            count += node.val * pow(10, i)
            i += 1
            node = node.next
        return count

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. 恢复成数字求和
        num1 = self.countNum(l1)
        num2 = self.countNum(l2)
        sum = num1 + num2
        if sum == 0:
            return ListNode(0)

        # 2. 拆分数字
        i = 1
        head = ListNode()
        last_node = head
        while sum != 0:
            val = sum % 10
            sum = sum // 10

            cur_node = ListNode(val)
            last_node.next = cur_node
            last_node = cur_node
            i += 1
        return head.next


if __name__ == '__main__':
    i = 1
    sum = 123
    array = []
    while sum != 0:
        val = sum % 10
        sum = sum // 10
        array.append(val)
        i += 1
    print(array)
