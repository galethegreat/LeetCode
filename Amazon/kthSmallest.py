import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        #TODO: check if matrix is less than k or == 1

        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])
        answer = list()

        for row in range(num_of_rows):
            if len(answer) == k and matrix[row][0] > -answer[0]: break


            for column in range(num_of_columns):
                if len(answer) < k:
                    heapq.heappush(answer, -matrix[row][column])
                elif matrix[row][column] <= -answer[0]:
                    heapq.heapreplace(answer, -matrix[row][column])
                else:break

        return -answer[0]

matrix = [[-5]]
k = 1
print(Solution().kthSmallest(matrix,k))
