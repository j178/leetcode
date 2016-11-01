# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self._isValidBST(root, float('-inf'), float('inf'))

    def _isValidBST(self, node, min, max):
        if node is None:
            return True
        if node.val >= max or node.val <= min:
            return False
        return self._isValidBST(node.left, min, node.val) and self._isValidBST(node.right, node.val, max)
