'''
将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

'''

# Definition for a binary tree node.
import math
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = TreeNode()
        self.toBST(root, nums)
        return root

    def toBST(self, root: TreeNode, nums: List[int]):
        # 取出中间数
        index = int(len(nums) / 2)
        root.val = nums[index]
        if len(nums[:index]) > 0:
            root.left = TreeNode()
            self.toBST(root.left, nums[:index])
        if len(nums[index + 1:]) > 0:
            root.right = TreeNode()
            self.toBST(root.right, nums[index + 1:])
        return
