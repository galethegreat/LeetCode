class Solution(object):
    def plusOne(self, digits):
        number_of_digits =  len(digits)
        #digits_copy = digits.copy()
        carry = 0
        index = 1


        new_digit_mod = (digits[-index] +1 ) %10
        carry = (digits[-index] +1  )// 10
        digits[-index] = new_digit_mod
        index +=1
        while(index <= number_of_digits and carry != 0):


            new_digit_mod = (digits[-index] +carry ) %10
            carry = (digits[-index] +carry  )// 10
            digits[-index] = new_digit_mod
            index += 1

        if carry != 0:
            digits.insert(0,carry)

        return digits
    def bruteForce(self, digits):
        lis = list()

        for digit in digits:
            lis.append(str(digit))

        #print(lis)
        digits_as_string = "".join(lis)
        digits_as_int = int(digits_as_string)

        answer = digits_as_int + 1
        answer_as_str = str(answer)
        answer_list = list()
        for character in answer_as_str:
            answer_list.append(int(character))
        return answer_list




x = Solution().plusOne([1,2,3])
print(x)
