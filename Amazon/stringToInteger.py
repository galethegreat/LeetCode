class Solution:
    def myAtoi(self, s):

        allowed_digits = set(['0','1','2','3','4','5','6','7','8','9'])
        string_in = s.strip()
        parse_str = list()
        isPos = None
        if len(string_in) == 0: return 0

        if string_in[0] == '-':
            isPos = False
        elif string_in[0] == '+':
            isPos = True

        if isPos is None:
            for index in range(len(string_in)):
                if string_in[index] in allowed_digits:
                    parse_str.append(string_in[index])
                else:break
        else:
            for index in range(1,len(string_in)):
                if string_in[index] in allowed_digits:
                    parse_str.append(string_in[index])
                else:break

        if len(parse_str) == 0: return 0

        extracted_int = int("".join(parse_str))

        if isPos == False:
            extracted_int = extracted_int*-1


        if extracted_int > 2**31 - 1:
            extracted_int = 2**31 - 1
        elif extracted_int < -2**31 :
            extracted_int = -2**31


        return extracted_int

def main():
    s =  "+"

    print((Solution().myAtoi(s)))

if __name__ == "__main__":
    main()
