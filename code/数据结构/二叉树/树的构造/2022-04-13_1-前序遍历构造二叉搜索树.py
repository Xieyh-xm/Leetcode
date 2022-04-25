'''
前序遍历构造二叉搜索树
给定一个整数数组，它表示BST(即 二叉搜索树 )的 先序遍历 ，构造树并返回其根。
保证 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。
二叉搜索树 是一棵二叉树，其中每个节点， Node.left 的任何后代的值 严格小于 Node.val , Node.right 的任何后代的值 严格大于 Node.val。
二叉树的 前序遍历 首先显示节点的值，然后遍历Node.left，最后遍历Node.right。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

'''二分查找左右子树的分界线递归构建左右子树
   时间复杂度：O(Nlog N)，在找左右子树分界线的时候时间复杂度为 O(log N)；
   空间复杂度：O(N)。'''
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def findIdx(val,lo,hi):
            # 在区间中找到第一个大于val的idx
            for i in range(lo,hi+1):
                if preorder[i]>val:
                    return i
            return -1  # 没有就返回-1
        def build(lo,hi)->TreeNode:
            if lo>hi and lo>=0:
                return None
            root=TreeNode(preorder[lo])
            right_tree_start=findIdx(root.val,lo,hi)
            root.left=build(lo+1,right_tree_start-1)
            root.right=build(right_tree_start,hi)
            return root
        return build(0,len(preorder)-1)