'''
删除链表的倒数第N个节点
给你一个链表，删除链表的倒数第个结点，并且返回链表的头结点。
---------------------------------------------
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
---------------------------------------------
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''方法一：非递归解决'''
        '''方法二：双指针'''
        cur_node = head

        while 1:
            next_n_node = cur_node

            for i in range(n):
                if next_n_node.next == None:
                    head = head.next
                    return head
                next_n_node = next_n_node.next
            if next_n_node.next == None:
                cur_node.next.val = None
                cur_node.next = cur_node.next.next
                return head
            cur_node = cur_node.next
        return head
