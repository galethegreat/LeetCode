class Solution(object):
    def findNumbers(self, nums):

        even_numer_of_digits = 0

        for num in nums:

            if len(str(num)) % 2 == 0:
                even_numer_of_digits += 1

        return even_numer_of_digits


user_input = [12,345,2,6,7896]
print(Solution().findNumbers(user_input))
