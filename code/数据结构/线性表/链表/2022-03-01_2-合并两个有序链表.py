'''
合并两个有序链表
---------------------------------------------
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

输入：l1 = [], l2 = []
输出：[]
---------------------------------------------
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 == None:
        #     return list2
        # elif list2 == None:
        #     return list1
        #
        # if list1.val <= list2.val:
        #     head = list1
        #     list1 = list1.next
        # else:
        #     head = list2
        #     list2 = list2.next
        #
        # cur_node = head
        # while 1:
        #     if list1 == None:
        #         cur_node.next = list2
        #         return head
        #     elif list2 == None:
        #         cur_node.next = list1
        #         return head
        #     # 比较哪个小
        #     if list1.val <= list2.val:
        #         cur_node.next = list1
        #         list1 = list1.next
        #     else:
        #         cur_node.next = list2
        #         list2 = list2.next
        #     cur_node = cur_node.next

        prehead = ListNode(-1)

        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = list1 if list1 is not None else list2

        return prehead.next
