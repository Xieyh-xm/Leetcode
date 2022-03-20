'''
寻找重复的子树

给定一棵二叉树 root，返回所有重复的子树。
对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
如果两棵树具有相同的结构和相同的结点值，则它们是重复的。

输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from platform import node
from typing import List, Optional

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count=collections.Counter()
        ans=[]
        def similarTree(node:TreeNode):
            if node==None:return "#"
            serial="{},{},{}".format(node.val,similarTree(node.left),similarTree(node.right))
            count[serial]+=1
            if count==2:
                ans.append(node)
        similarTree(root)
        return ans

        