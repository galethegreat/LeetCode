# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution:
    def intToRoman(self, num):

        roman_letters = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        digit = 1000

        answer = list()

        while digit >= 1:

            current_digit = num // digit
            num = num % digit

            if current_digit >= 1 and current_digit <= 3:
                answer.append(roman_letters[digit]*current_digit)
            elif current_digit == 5:
                answer.append(roman_letters[digit*5])
            elif current_digit >= 6 and current_digit <= 8:
                answer.append(roman_letters[digit*5])
                answer.append(roman_letters[digit]*(current_digit-5))
            elif current_digit == 4:
                answer.append(roman_letters[digit])
                answer.append(roman_letters[digit*5])
            elif current_digit == 9:
                answer.append(roman_letters[digit])
                answer.append(roman_letters[digit*10])

            digit = digit // 10

        return "".join(answer)

def main():

    num = 3999
    print((Solution().intToRoman(num)))

if __name__ == "__main__":
    main()
