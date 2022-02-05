from collections import deque

class Solution(object):
    def cutOffTree(self, forest):

        def bfs(vis, forest, start_row, start_col, end_row, end_col):

            if (start_row, start_col) == (end_row, end_col): return 0

            steps_taken = 0

            q = deque()
            visited = set()
            q.append((start_row, start_col))
            visited.add((start_row, start_col))

            while q:

                q_size = len(q)

                k = 0

                while k < q_size:
                    row, col = q.popleft()
                    visited.add((row, col))
                    if (row,col) == (end_row, end_col): return steps_taken

                    if row - 1 >= 0 and (row-1,col) not in visited and forest[row-1][col] != 0:
                         q.append((row-1,col))
                         visited.add((row-1,col))
                    if row + 1 < len(forest) and (row+1,col) not in visited and forest[row+1][col] != 0:
                         q.append((row+1,col))
                         visited.add((row+1,col))
                    if col - 1 >= 0 and (row,col-1) not in visited and forest[row][col-1] != 0:
                        q.append((row,col-1))
                        visited.add((row,col-1))
                    if col + 1 < len(forest[0]) and (row,col+1) not in visited and forest[row][col+1] != 0:
                        q.append((row,col+1))
                        visited.add((row,col+1))
                    k += 1

                steps_taken += 1

            return None

        if len(forest) == 0 or len(forest[0]) == 0 : return 0
        #if forest[0][0] == 0: return 0
        num_of_rows = len(forest)
        num_of_columns = len(forest[0])

        steps = 0
        trees = list()

        for row in range(num_of_rows):
            for col in range(num_of_columns):
                if forest[row][col] > 1: trees.append((forest[row][col], (row, col)))

        trees.sort()
        vis = 0
        coordinate = (0, 0)
        current_height = forest[0][0]

        for tree in trees:

            tree_coord = tree[1]
            step_to_next_tree = bfs(vis, forest, coordinate[0], coordinate[1], tree_coord[0], tree_coord[1])

            if step_to_next_tree is None: return -1

            steps += step_to_next_tree
            coordinate = tree_coord

        return steps

def main():
    forest  =  [[1,2,3],
                [0,0,4],
                [7,6,5]]
    print(Solution().cutOffTree(forest))

if __name__ == "__main__":
    main()
