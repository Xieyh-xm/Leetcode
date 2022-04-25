'''
N 叉树的前序遍历
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]
'''


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''递归'''
        def helper(node:Node):
            if node==None:
                return
            ret.append(node.val)
            for ch in node.children:
                helper(ch)          
        ret=[]
        helper(root)
        return ret
    
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''迭代'''
        ret=[]
        stack=[]
        stack.append(root)
        while stack:
            tmp_node=stack.pop()
            if tmp_node==None:
                continue
            ret.append(tmp_node.val)
            for ch in reversed(tmp_node.children):
                stack.append(ch)
        return ret