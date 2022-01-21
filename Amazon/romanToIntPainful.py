class Solution:
    def romanToInt(self, num_str):

        roman_numbers = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        roman_letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        digit = 1000
        current_digit = 0
        answer = list()
        char_pos = 0
        answer = 0
        while char_pos < len(num_str):

            if num_str[char_pos] == 'I' or num_str[char_pos] == 'X' or num_str[char_pos] == 'C' or num_str[char_pos] == 'M':
                current_digit = roman_letters[num_str[char_pos]]
                if (char_pos + 1) < len(num_str) and num_str[char_pos+1] == roman_numbers.get((current_digit*10), None):
                    current_digit = roman_letters[roman_numbers[current_digit*10]] - roman_letters[num_str[char_pos]]
                    char_pos += 2
                elif (char_pos + 1) < len(num_str) and num_str[char_pos+1] == roman_numbers.get((current_digit*5),None):
                    current_digit = roman_letters[roman_numbers[current_digit*5]] - roman_letters[num_str[char_pos]]
                    char_pos += 2
                elif (char_pos + 1) < len(num_str) and num_str[char_pos + 1] == roman_numbers.get(current_digit//10,None):
                    current_symbol =  roman_numbers[current_digit//10]
                    char_pos += 1
                    if (char_pos + 1) < len(num_str) and num_str[char_pos+1] == roman_numbers.get(roman_letters[current_symbol] * 10, None):
                        current_digit += ( roman_letters[current_symbol] * 10 - roman_letters[current_symbol])
                        char_pos += 2
                    if (char_pos + 1) < len(num_str) and num_str[char_pos+1] == roman_numbers.get(roman_letters[current_symbol] * 5, None):
                        current_digit += ( roman_letters[current_symbol] * 5 - roman_letters[current_symbol])
                        char_pos += 2
                    else:
                        while char_pos < len(num_str) and num_str[char_pos] == current_symbol:
                            current_digit += roman_letters[current_symbol]
                            char_pos += 1

                elif (char_pos + 1) < len(num_str) and num_str[char_pos + 1] == roman_numbers.get(current_digit//2,None):
                    current_symbol =  roman_numbers[current_digit//2]
                    current_digit += roman_letters[current_symbol]
                    char_pos += 1

                    if (char_pos + 1) < len(num_str) and num_str[char_pos + 1] == roman_numbers.get(roman_letters[current_symbol] // 5,None):
                        new_symbol = roman_numbers.get(roman_letters[current_symbol]//5)

                        char_pos += 1
                        while char_pos < len(num_str) and num_str[char_pos] == new_symbol:
                            current_digit += roman_letters[new_symbol]
                            char_pos += 1
                    else:char_pos += 1

                elif (char_pos + 1) < len(num_str) and num_str[char_pos + 1] == roman_numbers.get(current_digit,None):
                    char_pos += 1
                    current_symbol =  roman_numbers[current_digit]
                    while char_pos < len(num_str) and num_str[char_pos] == current_symbol:
                        current_digit += roman_letters[current_symbol]
                        char_pos += 1
                else:
                    char_pos  += 1


            elif num_str[char_pos] == 'V' or num_str[char_pos] == 'L' or num_str[char_pos] == 'D':
                current_digit = roman_letters[num_str[char_pos]]
                if (char_pos + 1) < len(num_str) and num_str[char_pos + 1] == roman_numbers.get((current_digit/5),None):
                    current_symbol = roman_numbers[current_digit/5]
                    char_pos += 1
                    while char_pos < len(num_str) and num_str[char_pos] == current_symbol:
                        current_digit += roman_letters[current_symbol]
                        char_pos += 1
                else:
                    char_pos += 1

            answer += current_digit

        return answer

def main():

    num = "MMMCDXLIV"
    print((Solution().romanToInt(num)))

if __name__ == "__main__":
    main()
