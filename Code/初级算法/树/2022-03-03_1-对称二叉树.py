'''
对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。
---------------------------------------------
输入：root = [1,2,2,3,4,4,3]
输出：true
---------------------------------------------
进阶：你可以运用递归和迭代两种方法解决这个问题吗？
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root.right, root.left)

    def isMirror(self, treeNode_1: TreeNode, treeNode_2: TreeNode):
        if treeNode_1 == None and treeNode_2 == None:
            return True
        if treeNode_1 == None or treeNode_2 == None:
            return False
        return treeNode_1.val == treeNode_2.val and self.isMirror(treeNode_1.right, treeNode_2.left) and self.isMirror(
            treeNode_1.left, treeNode_2.right)
