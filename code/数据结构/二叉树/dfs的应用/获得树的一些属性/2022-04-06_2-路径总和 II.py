'''路径总和 II
给你二叉树的根节点 root 和一个整数目标和 targetSum，
找出所有从根节点到叶子节点路径总和等于给定目标和的路径。
叶子节点是指没有子节点的节点。

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def preorder(node:TreeNode,trace:list):
            # 避免函数内的运算，改变外部变量的值，但这么做空间开销很大
            t_trace=trace.copy()
            if node==None:
                return
            t_trace.append(node.val)
            if node.left==None and node.right==None:
                if sum(t_trace)==targetSum:
                    ans.append(t_trace)
                return
            preorder(node.left,t_trace) 
            preorder(node.right,t_trace)
            return
        ans=[]
        preorder(root,[])
        return ans
    
'''看看人家写的！！！'''
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = list()
        path = list()
        
        def dfs(root: TreeNode, targetSum: int):
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                ret.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            ## 这一步非常关键！注意一下！
            # 相当于遍历完左右孩子后，把当前节点从path中抛出
            path.pop()   
        
        dfs(root, targetSum)
        return ret
    
    

if __name__=='__main__':
    s=Solution()
    root=TreeNode(1)
    print(s.pathSum(root,1))