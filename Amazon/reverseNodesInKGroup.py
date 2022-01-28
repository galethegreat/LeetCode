class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):

        if head is None or head.next is None or k == 1: return head

        size_of_list = 0
        node = head

        while node:
            size_of_list += 1
            node = node.next

        num_of_reverses = size_of_list // k
        nodes_to_reverse = k

        prev = None
        cur = head
        new_head = None
        old_start = None
        while num_of_reverses > 0:

            start_node = cur

            while nodes_to_reverse > 0:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
                nodes_to_reverse -= 1


            end_node = prev

            if new_head is None:
                new_head = end_node
                old_start = start_node
            else:
                old_start.next = end_node
                old_start = start_node


            start_node.next = next_node
            cur = next_node
            prev = start_node

            nodes_to_reverse = k
            num_of_reverses -= 1

        return new_head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2
    ans = Solution().reverseKGroup(head, k)

    while ans:
        print(ans.val)
        ans = ans.next


if __name__ == "__main__":
    main()
