class Solution(object):
    def numberToWords(self, number):
        ones_to_words = {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', \
        5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}

        tens_to_words = {10: 'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', \
        14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen'\
        , 19:'Nineteen'}

        tenths_to_words = {2:'Twenty', 3:'Thirty', 4:'Forty', \
        5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}

        large_to_words = {100:'Hundred', 1000:'Thousand', 1000000:'Million', 1000000000:'Billion'}

        def helper_100(number):
            if number < 10: return ones_to_words[number]
            if number >= 10 and number < 20 and number: return tens_to_words[number]

            if number >= 20 and number < 100:
                return tenths_to_words[number // 10] + ' ' + ones_to_words[number % 10]

        def helper_1000(number):
            if number < 100 :
                return helper_100(number).rstrip()
            if number >= 100 and number < 1000:
                answer = ones_to_words[number//100] + " " + large_to_words[100] + " " + helper_100(number%100)
                return answer.rstrip()
        def helper_1000000(number):
            if number < 1000: return helper_1000(number).rstrip()
            if number >= 1000 and number < 1000000:
                return helper_1000(number//1000) + " " + large_to_words[1000] + " " + helper_1000(number % 1000)

        def b_helper(number):
            if number >= 1000000:
                return helper_1000(number//1000000) + " "+ large_to_words[1000000] + " " + helper_1000000(number%1000000)
            else:return helper_1000000(number).rstrip()

        if number == 0: return "Zero"
        if number < 1000: return helper_1000(number).rstrip()
        if number >= 1000 and number < 1000000: return helper_1000000(number).rstrip()
        if number >= 1000000 and number < 1000000000: return b_helper(number).rstrip()
        if number >= 1000000000:
            answer = helper_100(number//1000000000)+" " + large_to_words[1000000000] + " " + b_helper(number%1000000000)
            return answer.rstrip()



def main():

    number = 100000
    print(Solution().numberToWords(number))

if __name__ == "__main__":
    main()
