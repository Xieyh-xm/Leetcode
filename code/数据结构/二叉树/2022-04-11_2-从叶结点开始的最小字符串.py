'''
从叶结点开始的最小字符串
给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个 [0, 25] 范围内的值，分别代表字母 'a' 到 'z'。

返回 按字典序最小 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

注：字符串中任何较短的前缀在 字典序上 都是 较小 的：

例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。 
节点的叶节点是没有子节点的节点。
'''

# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def preOrder(node:TreeNode):
            if not node:
                return
            stack.append(chr(ord('a')+node.val))
            if not node.left and not node.right:
                print(stack[-1])
                curStr="".join(reversed(stack))
                if self.ans==None or curStr<self.ans:
                    self.ans=curStr
            preOrder(node.left)
            preOrder(node.right)
            stack.pop()
        stack=[]
        self.ans=None
        preOrder(root)
        return self.ans