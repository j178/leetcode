# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.


# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, min, max):
        if node is None:
            return True
        return (min < node.val < max
                and self.valid(node.left, min, node.val)
                and self.valid(node.right, node.val, max))


class Solution2:
    prev = None

    def isValidBST(self, root):
        return self.mononical_increasing(root)

    def mononical_increasing(self, node):
        if node is None:
            return True
        # 中序遍历
        if self.mononical_increasing(node.left):
            if self.prev is not None and self.prev.val > node.val:
                return False
            self.prev = node
            return self.mononical_increasing(node.right)
