'''
翻转二叉树
给你一棵二叉树的根节点 root，翻转这棵二叉树，并返回其根节点。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node:TreeNode):
            if node==None:
                return
            if node.left==None and node.right==None:
                return
            tmp=node.left
            node.left=node.right
            node.right=tmp
            
            invert(node.left)
            invert(node.right)
            return
        invert(root)
        return root
        