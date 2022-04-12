'''
从中序与后序遍历序列构造二叉树
给定两个整数数组 inorder 和 postorder ，
其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List

'''核心：左右中reversed后变成中右左，和前一题相比，左右子树的处理顺序变一下'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(node,lo,hi):
            if lo>hi:
                return None 
            node=TreeNode(postorder.pop(0))
            idx=inorder.index(node.val)
            node.right=build(node.right,idx+1,hi)
            node.left=build(node.left,lo,idx-1)
            return node
        postorder=postorder[::-1]
        root=TreeNode(postorder.pop(0))
        idx=inorder.index(root.val)
        root.right=build(root.right,idx+1,len(inorder)-1)
        root.left=build(root.left,0,idx-1)
        return root
