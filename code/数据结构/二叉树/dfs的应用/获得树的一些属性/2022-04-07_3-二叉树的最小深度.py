'''二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。说明：叶子节点是指没有子节点的节点。

输入：root = [3,9,20,null,null,15,7]
输出：2
'''

# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        global minLength
        minLength=sys.maxsize
        def findMin(node:TreeNode,curLength:int):
            global minLength
            if node==None:
                return
            curLength+=1
            if curLength>=minLength:
                return
            if node.left==None and node.right==None:
                minLength=min(curLength,minLength)
                return
            findMin(node.left,curLength)
            findMin(node.right,curLength)
        if root==None:
            return 0
        findMin(root,0)
        return minLength