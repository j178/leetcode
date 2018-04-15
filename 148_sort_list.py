# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 链表版的归并排序，merge 算法对链表有些不同
# 还有链表找中间点的方法

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 将链表一分为二
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)

    def merge(self, left, right):
        l = ListNode(0)  # 新的链表
        p = l

        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next

            p = p.next

        if left:
            p.next = left
        elif right:
            p.next = right

        return l.next
