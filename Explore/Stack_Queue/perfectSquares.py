class Solution(object):
    def numSquares(self, n):

        if n <= 1:
            return 1

        squares = list()

        for number in range(1,n):

            perfect_square = number * number
            if perfect_square > n: break
            squares.append(perfect_square)

        number_of_squares = list()
        number_of_squares.append(0)
        for number in range(1, n+1):
            values = []
            for square in squares:
                if number - square >= 0:
                    values.append(number_of_squares[number-square])
                else:break

            number_of_squares.append(min(values) + 1)

        return number_of_squares[-1]

print(Solution().numSquares(13))
