'''
路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum。判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和 targetSum。
如果存在，返回 true；否则，返回 false。
叶子节点是指没有子节点的节点。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def preorder(node:TreeNode,curSum:int):
            if node==None:
                return False
            if node.left==None and node.right==None:
                return (curSum+node.val)==targetSum
            curSum+=node.val
            return preorder(node.left,curSum) or preorder(node.right,curSum)
        if root==None:
            return False
        return preorder(root,0)
            