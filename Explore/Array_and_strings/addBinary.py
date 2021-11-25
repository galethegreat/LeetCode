class Solution(object):

    def addHelper(self, digit_a, digit_b, carry_in):

        result, carry = 0,0

        if digit_a == '0' and digit_b == '0':
            if carry_in:
                result = 1
            else:
                result = 0
        elif (digit_a == '0' and digit_b == '1' ) or (digit_a == '1' and digit_b == '0'):
            if carry_in:
                carry = 1
            else:
                result = 1
        else:
            if carry_in:
                result = 1
                carry = 1
            else:
                carry = 1

        return result, carry

    def addBinary(self, a, b):

        number_of_digits_in_a = len(a)
        number_of_digits_in_b = len(b)

        if number_of_digits_in_b < 1:
            return a
        result_digit_list =list()

        result_digit = 0
        carry = 0
        b = b[::-1]
        a = a[::-1]

        carry_left = 0
        if number_of_digits_in_a >= number_of_digits_in_b:

            for indexb in range(0,number_of_digits_in_b):
                result_digit, carry = self.addHelper(b[indexb],a[indexb],carry)
                result_digit_list.append(str(result_digit))

            for indexa in range(number_of_digits_in_b,number_of_digits_in_a):
                result_digit, carry_left = self.addHelper(str(carry),a[indexa],carry_left)
                carry = 0
                result_digit_list.append(str(result_digit))

            if carry:
                result_digit_list.append(str(carry))
            elif carry_left:
                result_digit_list.append(str(carry_left))

        if number_of_digits_in_a < number_of_digits_in_b:

            for indexa in range(0,number_of_digits_in_a):
                result_digit, carry = self.addHelper(b[indexa],a[indexa],carry)
                result_digit_list.append(str(result_digit))

            for indexb in range(number_of_digits_in_a,number_of_digits_in_b):
                result_digit, carry_left = self.addHelper(str(carry),b[indexb],carry_left)
                carry = 0
                result_digit_list.append(str(result_digit))

            if carry:
                result_digit_list.append(str(carry))
            elif carry_left:
                result_digit_list.append(str(carry_left))

        result_digit_list = "".join(result_digit_list[::-1])
        return result_digit_list





x = Solution().addBinary("1","1011")


print(x)

# probably how i should have sovled it:
# lass Solution:
#     def addBinary(self, a, b) -> str:
#         n = max(len(a), len(b))
#         a, b = a.zfill(n), b.zfill(n)
#
#         carry = 0
#         answer = []
#         for i in range(n - 1, -1, -1):
#             if a[i] == '1':
#                 carry += 1
#             if b[i] == '1':
#                 carry += 1
#
#             if carry % 2 == 1:
#                 answer.append('1')
#             else:
#                 answer.append('0')
#
#             carry //= 2
#
#         if carry == 1:
#             answer.append('1')
#         answer.reverse()
#
#         return ''.join(answer)

# the 300IQ solve
# class Solution:
#     def addBinary(self, a, b) -> str:
#         x, y = int(a, 2), int(b, 2)
#         while y:
#             answer = x ^ y
#             carry = (x & y) << 1
#             x, y = answer, carry
#         return bin(x)[2:]
