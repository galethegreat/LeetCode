class Solution:
    def romanToInt(self, num_str):

        roman_letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX':9 ,'XL':40, 'XC':90, 'CD':400, 'CM':900}

        answer = 0
        index = 0

        if len(num_str) == 1: return roman_letters[num_str[0]]

        while index < len(num_str) :

            if index < len(num_str) -1 and roman_letters[num_str[index]] < roman_letters[num_str[index+1]]:
                current_digit = roman_letters[num_str[index:index+2]]
                index += 2
            else:
                current_digit = roman_letters[num_str[index]]
                index += 1
            answer += current_digit

        return answer

def main():

    num = "III"
    print((Solution().romanToInt(num)))

if __name__ == "__main__":
    main()
