'''
N 叉树的后序遍历
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]
'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''递归'''
        def helper(node:Node):
            if not node:
                return
            for ch in node.children:
                helper(ch)
            ret.append(node.val)
            return
        ret=[]
        helper(root)
        return ret
    
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''迭代'''
        ret=[]
        stack=[]
        stack.append(root)
        while stack:
            tmp_node=stack.pop()
            if not tmp_node:
                continue
            ret.append(tmp_node.val)
            for ch in tmp_node.children:
                stack.append(ch)
        return list(reversed(ret))