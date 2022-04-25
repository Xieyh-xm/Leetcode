'''路径总和 III
给定一个二叉树的根节点 root，和一个整数 targetSum
求该二叉树里节点值之和等于 targetSum 的路径的数目。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import Optional

'''迭代中套一个迭代'''
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def rootSum(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)
            return ret
        
        if root is None:
            return 0
            
        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret
        
'''前缀和'''
# 带记忆的搜索
# 哈希表永远存储的是当前这条路径上的前缀和
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            ret = 0
            curr += root.val    # 计算前缀和
            # 如果curr - targetSum在哈希表中的映射为1，
            # 说明存在前缀和为curr - targetSum的节点，这个节点和当前节点之间节点的和就是target
            ret += prefix[curr - targetSum]     
            prefix[curr] += 1   # 将该前缀和加入哈希表
            ret += dfs(root.left, curr)    # 遍历左子树
            ret += dfs(root.right, curr)   # 遍历右子树
            # 注意，遍历完左右子树后，把这个节点的值删掉，
            # 因为下一个回合，他就已经不在当前路径上了
            prefix[curr] -= 1 

            return ret

        return dfs(root, 0)