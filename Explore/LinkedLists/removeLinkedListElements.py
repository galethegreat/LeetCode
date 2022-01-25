class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):

        node = head

        while node is not None and node.val == val:
            if node.next is not None:

                node.val = node.next.val
                node.next = node.next.next

            else:
                node.next = None
                node = None
                return node

        while node is not None:
            if node.next is not None and node.next.val == val:
                if node.next.next is not None:
                    temp_node = node.next.next
                    while temp_node.val == val:
                        temp_node = temp_node.next
                        if temp_node is None:break
                    node.next = temp_node
                else:
                    node.next = None

            node = node.next

        return head

obj = ListNode(1)
obj.next = ListNode(2)
obj.next.next  = ListNode(6)
obj.next.next.next  = ListNode(3)
obj.next.next.next.next = ListNode(4)
obj.next.next.next.next.next = ListNode(5)
obj.next.next.next.next.next.next = ListNode(6)

print(Solution().reverseList(obj))
