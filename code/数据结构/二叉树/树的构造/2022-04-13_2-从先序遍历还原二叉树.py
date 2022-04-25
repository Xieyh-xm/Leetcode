'''从先序遍历还原二叉树
我们从二叉树的根节点 root 开始进行深度优先搜索。
在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
（如果节点的深度为 D，则其直接子节点的深度为 D+1。根节点的深度为 0)。
如果节点只有一个子节点，那么保证该子节点为左子节点。
给出遍历输出 S，还原树并返回其根节点 root。

难得吐血...用迭代+栈，递归因为要传递太多变量，比较麻烦

输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        stack = [] #存节点
        while i < len(S):
            cur_level = 0
            while i<len(S) and S[i] == '-':#记录下一个节点是第几层的
                cur_level += 1
                i += 1
            cur_val = 0
            while i<len(S) and S[i] != '-':#记录当前节点的值
                cur_val = cur_val*10 + int(S[i])    
                i += 1
            node = TreeNode(cur_val)
            if not stack: #根节点，直接入栈
                stack.append(node)
                continue
            while len(stack) > cur_level:#此时爹还在更靠前的地方，需要把不是的pop掉
                stack.pop()
                
            if not stack[-1].left: #父节点左子节点为空则当前节点放左边，否则放右边
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)#当前节点入栈，等自己的儿子来找他
        
        return stack[0]#栈底一定是root            