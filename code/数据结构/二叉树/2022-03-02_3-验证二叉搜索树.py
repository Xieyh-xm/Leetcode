'''
验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
---------------------------------------------
输入：root = [2,1,3]
输出：true
---------------------------------------------
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''注意：局部合法性不能代表全局的合法性！！！
                不能简单地判断当前节点与左右子节点的合法关系。
                需要使用带信息的递归'''
        return self.isValidBST_sub(root)

    def isValidBST_sub(self, root, min=float('-inf'), max=float('inf')):
        if root == None:
            return True
        if min >= root.val or root.val >= max:
            return False
        return self.isValidBST_sub(root.left, min, root.val) and self.isValidBST_sub(root.right, root.val, max)
