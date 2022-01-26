class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visited = dict()
    def copyRandomList(self, head):
        if head is None: return None

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val,None,None)

        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random =  self.copyRandomList(head.random)

        return node

def main():
    head = Node()

    ans = Solution().copyRandomList(head)

    ans_list = list()
    while ans is not None:
        ans_list.append(ans.val)
        ans = ans.next
    print( ans_list)
#print ans for troubleshooting purposes


if __name__ == "__main__":
    main()
