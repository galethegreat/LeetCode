class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None: return None
        if list1 is None and list2 is not None: return list2
        if list1 is not None and list2 is None: return list1
        node_ans = ListNode(0) #sentinel node
        node_ans_head = node_ans
        node1 = list1
        node2 = list2

        while node1 and node2:
            if node1.val <= node2.val:
                node_ans.next = node1
                node1 = node1.next
            else:
                node_ans.next = node2
                node2 = node2.next

            node_ans = node_ans.next

        if node1 is None and node2 is not None:
                node_ans.next = node2

        elif node1 is not None and node2 is None:
                node_ans.next = node1

        return node_ans_head.next

def main():
    li1 = ListNode(1)
    li1.next = ListNode(2)
    li1.next.next = ListNode(4)

    li2 = ListNode(1)
    li2.next = ListNode(3)
    li2.next.next = ListNode(4)
    #li2 = None
    ans = Solution().mergeTwoLists(li1,li2)

#print ans for troubleshooting purposes
    ans_list = list()
    node = ans
    while node is not None:
        ans_list.append(node.val)
        node = node.next
    print(ans_list)

if __name__ == "__main__":
    main()
