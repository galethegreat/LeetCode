class Solution(object):
    def getIntersectionNode(self, head_a, head_b):

        if head_a is None or head_b is None: return None
        p1 = head_a
        p2 = head_b

        while p1 != p2:

            if p1 is not None: p1 = p1.next
            else: p1 = head_b

            if p2 is not None: p2 = p2.next
            else: p2 = head_a

        return p1
