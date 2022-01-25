class Solution(object):
    def removeNthFromEnd(self, head, n):

        size_of_list = 0
        node  = head
        while node is not None:
            node = node.next
            size_of_list += 1

        if size_of_list == 1 and n == 1:
            head = None
            return head

        if size_of_list > 1 and n == size_of_list:
            new_head = head.next
            head = new_head
            return head
            
        node_index_to_delete  = size_of_list - n
        node_index = 0
        node = head
        while node_index < node_index_to_delete - 1:
            node = node.next
            node_index += 1

        node_to_delete = node.next
        node_to_replace = node.next.next
        node.next = node_to_replace

        return head
