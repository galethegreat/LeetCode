class Solution():
    def merge(self, n_1, n_2):

        p1 = 0
        p2 = 0
        r1 = len(n_1)
        r2 = len(n_2)
        answer = list()

        while p1 < r1 and p2 < r2:
            if n_1[p1] <= n_2[p2]:

                answer.append(n_1[p1])
                p1 += 1
            else:
                answer.append(n_2[p2])
                p2 += 1

        if p1 >= r1 and p2 < r2:
            answer = answer + n_2[p2:]

        elif p2 >= r2 and p1 < r1:
            answer = answer + n_1[p1:]

        return answer



    def sortArray(self, nums):
        if len(nums) <= 1 :
            return nums

        midpoint = len(nums) // 2


        left = self.sortArray(nums[0:midpoint])
        right = self.sortArray(nums[midpoint:])

        return self.merge(left, right)



def main():

    l2 = [7,2,3,8]
    print(Solution().sortArray(l2))

if __name__ == "__main__":
    main()
