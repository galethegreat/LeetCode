class Solution(object):
    def isValid(self,s):
        if len(s) <=1: return False

        open_parentheses = ['(','[','{']
        pairing = {'(':')','[':']','{':'}'}
        stack = list()

        for bracket in s:
            if bracket in open_parentheses:
                stack.append(bracket)
            elif len(stack) > 0:
                bracket_to_close = stack.pop()
                if bracket != pairing[bracket_to_close]:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False
        else:
             return True


def main():
    brackets = ")()"

    print((Solution().isValid(brackets)))

if __name__ == "__main__":
    main()
