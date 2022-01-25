class Solution(object):
    def removeNthFromEnd(self, head, n):

        p_after = head

        for _ in range(n):
            p_after = p_after.next

        if p_after is None: return head.next

        p_before = head

        while p_after.next is not None:
            p_before = p_before.next
            p_after = p_after.next

        p_before.next = p_before.next.next
        return head
