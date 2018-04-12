# Created by John Jiang at 2018/4/12 20:24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# http://www.cnblogs.com/dolphin0520/archive/2011/08/25/2153720.html

class Solution:
    def preorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if not root:
            return result

        current = root
        while current:
            result.append(current.val)
            if current.right:
                stack.append(current.right)

            current = current.left
            if current is None and stack:
                current = stack.pop()

        return result

    def preorder_traversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if not root:
            return result

        current = root
        while current or stack:
            while current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            current = stack.pop()
            current = current.right

        return result

    def inorder_traversal(self, root):
        result = []
        stack = []
        if not root:
            return result

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root)
            root = root.right

    def postorder_traversal(self, root):
        result = []
        stack = []
        if not root:
            return result

        while root or stack:
            while root:
                root.first = True
                stack.append(root)
                root = root.left

            tmp = stack.pop()
            # 第一次出现在栈顶，此时此节点右子树还没有处理
            if tmp.first:
                tmp.first = False
                stack.append(tmp)
                root = tmp.right
            # 节点第二次出现在栈顶
            else:
                result.append(tmp)
                root = None
