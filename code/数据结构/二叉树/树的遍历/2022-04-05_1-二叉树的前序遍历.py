'''
二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''递归写法'''
        # def preorder(root:TreeNode):
        #     if root==None:
        #         return
        #     res.append(root.val) # 根节点在前
        #     preorder(root.left)
        #     preorder(root.right)
        # res=[]
        # preorder(root)
        # return res
        
        '''迭代写法
        也可以用迭代的方式实现方法一的递归函数，两种方式是等价的，
        区别在于递归的时候隐式地维护了一个栈，而我们在迭代的时候需要显式地将这个栈模拟出来，
        其余的实现与细节都相同'''
        ans=[]
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if node==None:
                continue
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return ans    
        