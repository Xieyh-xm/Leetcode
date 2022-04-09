'''
二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''注意问题的拆解'''
'''思路：两个叶子节点之间的路径=根节点左右儿子的深度之和'''

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=0
        def depth(node:TreeNode)->int:
            if not node:
                return 0
            L=depth(node.left)
            R=depth(node.right)
            self.ans=max(self.ans,L+R)
            return max(L,R)+1
        depth(root)
        return self.ans
        