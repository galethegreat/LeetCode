class Solution(object):
    def validateBrackets(input):

        valid = {'(', ')', '[', ']', '{', '}'}
        brackets = {'(': ')', '[':']', '{':'}'}

        stack = list()

        for bracket in input:
            if bracket not in valid: continue
            
            if bracket in brackets:
                stack.append(brackets[bracket])
            elif stack:
                closing_bracket = stack.pop()
                if bracket != closing_bracket: return False
            else:
                return False

        if stack: return False
        return True
