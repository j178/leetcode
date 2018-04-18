# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 判断链表是否有环，用快慢指针追击的方式
        # 而判断环的起点，需要一定的技巧
        # http://bangbingsyb.blogspot.com/2014/11/leetcode-linked-list-cycle-i-ii.html
        # 总之，就是当 fast 与 slow 相遇后，将 slow 移回 head, 然后 slow 和 fast 一步步地走，再次相遇时的点，就是环开始的地方
        if not head:
            return None
        fast = slow = head

        while True:
            if not fast.next or not fast.next.next:
                # 无环
                return None
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
