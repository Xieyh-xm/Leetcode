

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''递归法'''
        # def inorder(root):
        #     if root==None:
        #         return
        #     inorder(root.left)
        #     ans.append(root.val)     
        #     inorder(root.right)   
        # ans=[]
        # inorder(root)
        # return ans
        '''迭代法'''
        '''中序遍历的不同之处在于二叉树的访问顺序和处理顺序不同'''
        ans,stack=[],[]
        cur=root
        while cur!=None or stack:
            if cur!=None:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                ans.append(cur.val)                
                cur=cur.right
        return ans
        
        
            
            
        
        