# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''递归写法'''
        # 左右中
        def postorder(node:TreeNode):
            if node==None:
                return
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)
        ans=[]
        postorder(root)
        return ans
        
        '''迭代法'''
        # stack=[root]
        # ans=[]
        # while stack:
        #     tmp=stack.pop()
        #     if tmp==None:
        #         continue
        #     # 中右左,左先压入栈
        #     ans.append(tmp.val)
        #     stack.append(tmp.left)
        #     stack.append(tmp.right)
        # return list(reversed(ans))
        