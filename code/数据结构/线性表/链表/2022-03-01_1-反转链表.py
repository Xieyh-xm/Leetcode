'''
反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
---------------------------------------------
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
---------------------------------------------
进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''方法一：递推法'''
        if head == None:
            return head
        elif head.next == None:
            return head
        cur_node = head.next
        next_node = cur_node.next
        head.next = None
        last_node = head
        while 1:
            # 从第二个节点开始调整
            cur_node.next = last_node  # 指向上一个指针
            if next_node == None:  # 到最后一个节点
                head = cur_node
                return head
            last_node = cur_node
            cur_node = next_node
            next_node = cur_node.next
        '''双百写法'''
        # last_head = None
        # while head:
        #     # 取出来下一个
        #     next = head.next
        #     # 把当前指向上一个
        #     head.next = last_head
        #     # 上一个的值指向当前，再下次循环中会被当成上一个值
        #     last_head = head
        #     # 头节点指向下一个值
        #     head = next
        # return last_head


if __name__ == '__main__':
    solution = Solution()
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    solution.reverseList(node1)
