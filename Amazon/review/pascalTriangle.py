class Solution(object):
    def generate(self, numRows):
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]

        answer = [[1],[1,1]]
        row = list()
        for n in range(2,numRows):
            row = [1]*(n+1)
            previousRow = answer[n-1]
            for element in range(1,len(row)-1):
                row[element] =  previousRow[element]+previousRow[element-1]
            answer.append(row)

        return answer


def main():
    numRows = 1
    print(Solution().generate(numRows))

if __name__ == "__main__":
    main()
