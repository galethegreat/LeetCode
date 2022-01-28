import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
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

    def mergeKLists(self, lists):
        if litsts is None: return None
        if len(lists) == 0 : return None
        if len(lists) == 1 and lists[0] is None: return None
        if len(lists) == 1 and lists[0] is not None: return lists
        li1 = sizes.pop()
        li2 = sizes.pop()
        l3 = self.mergeTwoLists(li1,li2)

        while len(sizes) > 0:
            li2 = sizes.pop()
            l3 = self.mergeTwoLists(li3,li2)

        return l3


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2
    ans = Solution().mergeKLists(head, k)

    while ans:
        print(ans.val)
        ans = ans.next


if __name__ == "__main__":
    main()
