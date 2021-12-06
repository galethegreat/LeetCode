class Solution(object):

    def findDisappearedNumbers(self, nums):

        numbers_seen = {}
        #could use a set if numbers in nums are guaranteed to not be duplicates
        answer = list()

        for num in nums:
            numbers_seen[num] = numbers_seen.get(num, 0) + 1

        for number in range(1,len(nums)+1):

            if number in numbers_seen : continue

            else: answer.append(number)

        return answer


def main():
    nums = [2,3,3,4,5,6,7,8,9,10,11]

    print(Solution().findDisappearedNumbers(nums))

if __name__ == "__main__":
    main()
