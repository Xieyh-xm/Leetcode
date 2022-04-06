'''
二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的层序遍历 。 （即逐层地，从左到右访问所有节点）。
---------------------------------------------
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
---------------------------------------------
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        result = self.addNum(root, 0, result)
        return result

    def addNum(self, root: TreeNode, index: int, result):
        if root == None:
            return result
        if index >= len(result):
            result.append([])
        result[index].append(root.val)
        result = self.addNum(root.left, index + 1, result)
        result = self.addNum(root.right, index + 1, result)
        return result
