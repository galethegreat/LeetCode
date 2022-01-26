class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1, list2):

        node_ans = ListNode(0)
        node_ans_head = node_ans
        node1 = list1
        node2 = list2
        carry = 0
        value = 0

        while node1 and node2:

            value = (node1.val + node2.val + carry) % 10
            node_ans.next = ListNode(value)
            carry = (node1.val + node2.val + carry) // 10
            node1 = node1.next
            node2 = node2.next
            node_ans = node_ans.next

        if node1 is None and node2 is not None:
            while node2:
                value = (node2.val + carry) % 10
                node_ans.next = ListNode(value)
                carry = (node2.val + carry) // 10
                node_ans = node_ans.next
                node2 = node2.next

        elif node1 is not None and node2 is None:
            while node1:
                value = (node1.val + carry) % 10
                node_ans.next = ListNode(value)
                carry = (node1.val + carry) // 10
                node_ans = node_ans.next
                node1 = node1.next

        while carry > 0:
            value = (carry) % 10
            node_ans.next = ListNode(value)
            carry = (carry) // 10
            node_ans = node_ans.next
            
        return node_ans_head.next

def main():
    li1 = ListNode(3)
    li1.next = ListNode(7)

    li2 = ListNode(9)
    li2.next = ListNode(2)
    #li2.next.next = ListNode(4)
    #li2 = None
    ans = Solution().addTwoNumbers(li1,li2)
    #print(ans)

    ans_list = list()
    while ans is not None:
        ans_list.append(ans.val)
        ans = ans.next
    print( ans_list)
#print ans for troubleshooting purposes


if __name__ == "__main__":
    main()
