'''
回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
---------------------------------------------
输入：head = [1,2,2,1]
输出：true

输入：head = [1,2]
输出：falses
---------------------------------------------
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''方法一：暴力解法,读入数组'''
        prev = head
        array = []
        while prev:
            array.append(prev.val)
            prev = prev.next
        for i in range(len(array) // 2):
            if array[i] != array[-i - 1]:
                return False
        return True
