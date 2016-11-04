from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder(self, node):
    """递归版本中序遍历"""
    if node is None:
        return
    self.inorder(node.left)
    print(node.val)
    self.inorder(node.right)


def inorder_iter(self, root):
    """
    非递归中序遍历
    对于任一节点P:
    1. 如果 P 非空, 则将 P 入栈, P = P.left, 继续直到 P 为空
    2. 如果 P 为空, 取栈顶元素作为 P, 处理 P 的数据, 然后 P = P.right
    3. 直到 P 为空 或者栈为空
    """
    p = root
    s = []
    while p or s:
        while p:
            s.append(p)
            p = p.left
        if s:
            p = s.pop()
            print(p.val)
            p = p.right


def inorder_iter1(self, root):
    """中序遍历简单一点的写法"""
    s = []
    while root or s:
        if root:
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            print(root.val)
            root = root.right


def preorder_iter(self, root):
    """先序遍历"""
    p = root
    s = []
    while p or s:
        while p:
            print(p.val)
            s.append(p)
            p = p.left
        if s:
            p = s.pop()
            p = p.right


def postorder_iter(self, root):
    """
    前序和中序遍历的程序中，当我们准备进入根结点的右子树时，根结点就被扔出栈外了。但在后序遍历时，我们仍需保留它，直到右子树处理完毕。
    首先想到的改动就是在上面的程序的第9行到11行，不要从栈s中将根结点弹出，而是直接开始处理右子结点。
    但这就会带来一个问题：什么时候弹出根结点？实际上当左子树遍历完成、或者右子树遍历完成时，我们都会在栈里看到根结点，
    为了区分这两种状态，添加一个临时变量记录前一次访问的结点，如果前一个结点是根结点的右子树，就说明左右子树全都遍历完成了
    """
    s = []
    pre = None
    while root or s:
        if root:
            s.append(root)
            root = root.left
        elif s[-1].right != pre:
            root = s[-1].right
            pre = None
        else:
            pre = s.pop()
            print(pre.val)


def level_order(self, root):
    """层序遍历"""
    if not root: return
    q = deque([root])
    while q:
        root = q.popleft()
        print(root.val)
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
