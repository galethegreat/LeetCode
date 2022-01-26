class ListNode:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal):

        insert_node = ListNode(insertVal)

        if head is None:
            head = insert_node
            head.next = head
            return head

        if head.next == head:
            insert_node.next = head
            head.next = insert_node
            return head



        node = head
        start_node = node

        smallest_value = (node.val, node)
        biggest_value = (node.val, node)

        node = node.next

        while node != start_node:
            if node.val < smallest_value[0]:
                smallest_value = (node.val, node)

            if node.val > biggest_value[0]:
                biggest_value = (node.val, node)

            node = node.next

        if smallest_value[0] == insertVal:
            node = smallest_value[1]
            temp_node = node.next
            node.next = insert_node
            insert_node.next = temp_node
            return head
        if insertVal > smallest_value[0]:
            node = smallest_value[1]
            prev = node
            while prev.next != node:
                if prev.next.val >= insertVal:
                    temp_node = prev.next
                    prev.next = insert_node
                    insert_node.next = temp_node
                    return head
                prev = prev.next
            prev.next = insert_node
            insert_node.next = node
            return head
        else:
            node = biggest_value[1]
            temp_node = node.next
            node.next = insert_node
            insert_node.next = temp_node
            return head



def main():
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = head

    ans = Solution().insert(head,2)
    ans_list = list()
    visited = set()
    while ans is not None and ans not in visited:
        visited.add(ans)
        ans_list.append(ans.val)
        ans = ans.next
    print( ans_list)


if __name__ == "__main__":
    main()
