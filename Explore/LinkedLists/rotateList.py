class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next


class Solution:

    def rotateRight(self, head, k):
        if head is None: return None
        if head.next is None or k == 0: return head

        node = head
        size_of_list = 0

        while node:
            size_of_list += 1
            end_node = node
            node = node.next

        end_node.next = head
        node = head
        num_of_rotations = size_of_list - (k % size_of_list)
        if num_of_rotations == 0: return head

        while num_of_rotations > 0:
            prev = node
            node = node.next
            num_of_rotations -= 1

        prev.next = None

        return node


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    k = 7
    ans = Solution().rotateRight(head, k )

    ans_list = list()
    while ans is not None:
        ans_list.append(ans.val)
        ans = ans.next
    print( ans_list)
#print ans for troubleshooting purposes


if __name__ == "__main__":
    main()
