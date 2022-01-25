class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):


    #proper way
    def oddEvenList(self, head):
        if head is None: return head
        odd = head
        even = head.next
        even_head = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    # my way (still O(n) tme and O(1) space)
    def oddEvenList(self, head):
        if head is None: return head
        if head.next is None : return head
        if head.next.next is None: return head
        prev = None
        node = head
        index = 1
        isEven = False
        while node.next is not None:
            prev = node
            node = node.next
            index += 1
        if index % 2 == 0:
            termination_node = prev
            end_node = node
            isEven = True
        else:
            termination_node = node
            end_node = termination_node
        node = head
        new_index = 1
        while node != termination_node:
          back_of_the_line_node = node.next
          node.next = node.next.next
          end_node.next = back_of_the_line_node
          end_node = back_of_the_line_node
          end_node.next = None
          node = node.next
          new_index += 1
        if isEven:
            print(node.val)
            back_of_the_line_node = node.next
            node.next = node.next.next
            end_node.next = back_of_the_line_node
            end_node = back_of_the_line_node
            end_node.next = None
        return head
        # ans = list()
        # node = head
        # visited = set()
        # while node is not None:
        #     if node not in visited:
        #         visited.add(node)
        #         ans.append(node.val)
        #     else:
        #         ans.append(f"{node.val} is cycle")
        #         break
        #     node = node.next
        # return ans

def main():
    head  = ListNode(1)
    head.next = ListNode(2)
#    head.next.next  = ListNode(3)
#    head.next.next.next   = ListNode(4)
    #head.next.next.next.next    = ListNode(5)

    print(Solution().oddEvenList(head))

if __name__ == "__main__":
    main()
