class Solution:
    def __init__(self):
        self.answer = list()

    def inorderTraversal(self,root):
        def inorderTraversalR(root):
            if root:
                if root.left == None and root.right== None and root.val != None:
                    self.answer.append( root.val)
                    if self.answer[-1] is None: self.answer.pop()

                else:
                    if root.left != None:
                        self.answer.append(inorderTraversalR(root.left))
                        if self.answer[-1] is None: self.answer.pop()
                    if root:
                        self.answer.append(root.val)
                        if self.answer[-1] is None: self.answer.pop()
                    if root.right != None:
                        self.answer.append(inorderTraversalR(root.right))
                        if self.answer[-1] is None: self.answer.pop()


        inorderTraversalR(root)
        return self.answer


tree =  [1,2,3]

print(Solution().inorderTraversal(tree))
