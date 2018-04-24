# Created by j178 at 2018/04/24 23:01

"""
117 Populating Next Right Pointers in Each Node II

Given a binary tree
    
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no
next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

**Note:**

  * You may only use constant extra space.
  * Recursive approach is fine, implicit stack space does not count as extra space for this problem.

**Example:**

Given the following binary tree,
    
         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL


AC Rate: 33.9%

Sample Test Case:
  {}

"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


from collections import deque


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = deque()
        sep = object()
        q.append(root)
        q.append(sep)

        while q:
            node = q.popleft()

            if node is sep:
                break

            last_level_end = False
            if q[0] is sep:
                q.popleft()
                last_level_end = True
                node.next = None
            else:
                node.next = q[0]

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if last_level_end:
                q.append(sep)

    def connect2(self, root):
        dummy = TreeLinkNode(0)
        while root:
            curr = dummy
            # 遍历一层，连接下一层的 next 指针
            while root:
                if root.left:
                    # 第一次循环，dummy.next 指向下一层的第一个节点
                    curr.next = root.left
                    curr = curr.next
                if root.right:
                    curr.next = root.right
                    curr = curr.next
                # 如果此时 root 为 None, 则遍历完了一层
                root = root.next

            root = dummy.next
            dummy.next = None


if __name__ == '__main__':
    s = Solution()
    root = TreeLinkNode(0)
    root.left = TreeLinkNode(1)
    root.right = TreeLinkNode(2)
    root.left.left = TreeLinkNode(3)
    root.left.right = TreeLinkNode(4)
    root.right.left = TreeLinkNode(5)
    root.right.right = TreeLinkNode(6)
    s.connect(root)
