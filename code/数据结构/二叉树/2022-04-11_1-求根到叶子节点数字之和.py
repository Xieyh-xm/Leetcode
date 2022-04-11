'''
求根到叶子节点数字之和
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：
    - 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
      计算从根节点到叶节点生成的 所有数字之和 。
叶节点 是指没有子节点的节点。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        '''方法一：多用了一个stack的空间'''
        # 栈->数
        def stackToNum(stack:list)->int:
            num=0
            for i in range(len(stack)):
                num+=stack[-1-i]*pow(10,i)
            return num
        # 前序遍历
        def preOrder(node:TreeNode):
            if node==None:
                return
            stack.append(node.val)
            # 到叶子节点的时候计算值
            if not node.right and not node.left:
                self.sum+=stackToNum(stack)
            preOrder(node.left)     # 遍历左子树
            preOrder(node.right)    # 遍历右子树
            # 弹出
            stack.pop()
        self.sum=0
        stack=[]
        preOrder(root)
        return self.sum

'''方法二：看看人家写的。。。'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)