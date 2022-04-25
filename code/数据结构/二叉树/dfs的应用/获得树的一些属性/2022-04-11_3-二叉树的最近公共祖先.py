'''
二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''当节点 p, qp,q 在节点 rootroot 的异侧时，节点 rootroot 即为最近公共祖先'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''方法一：超出时间范围 nlogn'''
        # def findNode(node:TreeNode,p:TreeNode)->bool:
        #     if not node:
        #         return False
        #     elif node==p:
        #         return True
        #     else:
        #         return findNode(node.left,p) or findNode(node.right,p)
        # if not root:
        #     return None
        # # 公共节点在左子树
        # if findNode(root.left,p) and findNode(root.left,q):
        #     return self.lowestCommonAncestor(root.left,p,q)
        # # 公共节点在右子树
        # if findNode(root.right,p) and findNode(root.right,q):
        #     return self.lowestCommonAncestor(root.right,p,q)
        # # 公共节点分别在两侧
        # return root
        '''方法二'''
        # 定义规则：比如在某一棵子树上先找到了p，则无需继续遍历这棵子树，
        # 因为即使这棵子树有q，p也一定是q的祖先，也就是它们两个的最近公共祖先。
        if root==None or root==p or root==q:
            return root
        # 按照上述规则，找到root的左子树的最近公共祖先。
        left=self.lowestCommonAncestor(root.left,p,q)
        # 按照上述规则，找到root的右子树的最近公共祖先。
        right=self.lowestCommonAncestor(root.right,p,q)
        # 一边找到了，一边没找到，根据上述规则，找到的就是最近公共祖先。
        if left==None:
            return right
        elif right==None:
            return left
        else:
            # 如果在左右子树分别找到了p和q，则说明root是它们两个的最近公共祖先。
            return root
        
        