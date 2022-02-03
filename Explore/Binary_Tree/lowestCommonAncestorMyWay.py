class Solution:

    def __init__(self):

        self.is_p_found = False
        self.is_q_found = False
        self.status = None

    def lowestCommonAncestor(self, root, p, q):

        def dfs(root, p, q):
            if root is None: return None
            if root in (p, q):
                if not self.is_p_found : self.is_p_found = root == p
                if not self.is_q_found : self.is_q_found = root == q

                status = [self.is_p_found,  self.is_q_found, None]

                if status[0] and status[1]: return status

                temp_status_l = dfs(root.left, p , q)
                temp_status_r = dfs(root.right, p , q)

                if temp_status_l is not None and temp_status_l[0] and temp_status_l[1]: status = (True, True, root)

                elif temp_status_r is not None and temp_status_r[0] and temp_status_r[1]:status = (True, True, root)

                return status

            status = dfs(root.left, p, q)

            if status is not None and status[2] is not None: return status

            temp_p, temp_q = self.is_p_found, self.is_q_found
            self.is_p_found, self.is_q_found = False, False

            status = dfs(root.right, p, q)

            self.is_p_found |= temp_p
            self.is_q_found |= temp_q

            status = [self.is_p_found, self.is_q_found, None] if status is None else [self.is_p_found, self.is_q_found, status[2]]

            if status is not None and status[2] is not None: return status

            elif status is not None and status[0] and status[1] and status[2] is None: status[2] = root

            return status

        if root is None or root == p or root == q: return root

        status = dfs(root.left, p, q)

        if self.is_p_found ^ self.is_q_found: return root

        elif status is not None and status[2] is not None: return status[2]
        status = dfs(root.right, p, q)

        return status[2]
