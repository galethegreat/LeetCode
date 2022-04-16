class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    #the correct solution and way to think about it
    def swapPairs(self,head):

        if not (head and head.next): return

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = head

        return second

    #my initial solution is more itarative then recursive

    def swapPairs(head):

        def swapHelper(root):
            if not (root.next and root.next.next): return head

            prev = root
            first = root.next
            second = root.next.next

            first.next, second.next = second.next, first
            prev.next = second

            swapHelper(first)

        if not head: return head

        start = ListNode(0, head)

        swapHelper(start)

        return start.next



def main():

if __name__ == '__main__':
    main()
