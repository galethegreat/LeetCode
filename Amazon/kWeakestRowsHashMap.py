import heapq
class Solution:
    def kWeakestRows(self, matrix, k):
        #TODO: check if matrix is less than k or == 1
        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])
        num_of_soldiers = None
        weakest_rows = list()
        for row in range(num_of_rows):
            num_of_soldiers = 0
            for column in range(num_of_columns):
                num_of_soldiers += matrix[row][column]
            weakest_rows.append((num_of_soldiers,row))
        weakest_rows.sort()
        answer = [row[1] for row in weakest_rows]

        return answer[0:k]
    #    heapq.heapify(weakest_rows)
        # for row in range(num_of_rows):
        #     num_of_soldiers = 0
        #     for column in range(num_of_columns):
        #         num_of_soldiers += matrix[row][column]
        #     if len(weakest_rows) < k:
        #         heapq.heappush(weakest_rows, (-num_of_soldiers, row))
        #     elif num_of_soldiers < -1*weakest_rows[0][0]:
        #         heapq.heapreplace(weakest_rows, (-num_of_soldiers, row))
        # print(weakest_rows)
        # weakest_rows.reverse()
        # print(weakest_rows)
        # answer = [row[1] for row in weakest_rows]
        return answer

matrix = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
print(Solution().kWeakestRows(matrix,k))
