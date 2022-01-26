class ListNode:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

class Solution:
    def flatten(self, head):

        def dfsLinkedList(head):
            head_node = head
            tail_node = head
            while head_node:
                if head_node.child is None:
                    if head_node.next is None: tail_node = head_node
                    head_node = head_node.next
                else:
                    next_node = head_node.next
                    dfs_head, dfs_tail = dfsLinkedList(head_node.child)

                    head_node.next = dfs_head
                    dfs_head.prev = head_node
                    if next_node is not None:
                        next_node.prev = dfs_tail
                        dfs_tail.next = next_node
                    else:
                        tail_node = dfs_tail
                    head_node.child = None
                    head_node = next_node

            return head, tail_node

        if head is None: return head
        node = head
        return dfsLinkedList(node)[0]

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    head.next.child = ListNode(4)
    head.next.child.next = ListNode(5)
    head.next.child.next.child = ListNode(6)
    head.next.child.next.child.next = ListNode(7)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    # head.next.next.child = ListNode(7)
    # head.next.next.child.next = ListNode(8)
    # head.next.next.child.next.child = ListNode(11)
    # head.next.next.child.next.child.next = ListNode(12)

    ans = Solution().flatten(head)

    ans_list = list()

    while ans is not None:
        ans_list.append(ans.val)
        ans = ans.next
    print( ans_list)


if __name__ == "__main__":
    main()
