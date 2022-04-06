'''
二叉树的最大深度
给定一个二叉树，找出其最大深度。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''方法一：深度优先搜索'''
        if root == None:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
