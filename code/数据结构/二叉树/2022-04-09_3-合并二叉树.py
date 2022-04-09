'''合并二叉树
给你两棵二叉树：root1 和 root2。
想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
否则，不为None的节点将直接作为新二叉树的节点。
返回合并后的二叉树。

注意：合并过程必须从两个树的根节点开始。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def merge(node1:TreeNode,node2:TreeNode)->TreeNode:
            if node1!=None and node2!=None:
                ret=TreeNode(node1.val+node2.val)
                ret.left=merge(node1.left,node2.left)
                ret.right=merge(node1.right,node2.right)
            elif node1!=None:
                ret=TreeNode(node1.val)
                ret.left=merge(node1.left,None)
                ret.right=merge(node1.right,None)
            elif node2!=None:
                ret=TreeNode(node2.val)
                ret.left=merge(None,node2.left)
                ret.right=merge(None,node2.right)
            else:
                return None
            return ret
        return merge(root1,root2)


'''看看人家写的！！！
少了很多额外空间，并且时间也更短'''   
class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""		
		def dfs(r1,r2):
			# 如果 r1和r2中，只要有一个是null，函数就直接返回
			if not (r1 and r2):
				return r1 if r1 else r2     # 减少时间消耗
			# 让r1的值 等于  r1和r2的值累加
			# 再递归的计算两颗树的左节点、右节点
			r1.val += r2.val
			r1.left = dfs(r1.left,r2.left)
			r1.right = dfs(r1.right,r2.right)
			return r1   # 利用r1的空间
		return dfs(t1,t2)


            
        
        
        
        