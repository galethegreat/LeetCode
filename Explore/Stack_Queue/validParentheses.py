class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0 :
            return False

        brackets_to_close = list()
        open_bracket = set(['(','{','['])

        corresponding_closed_bracket = {'(':')','[':']','{':'}'}

        for bracket in s:
            if bracket in open_bracket:
                brackets_to_close.append(corresponding_closed_bracket[bracket])
            else:
                if len(brackets_to_close) > 0:
                    next_bracket_to_close = brackets_to_close.pop()
                    if next_bracket_to_close == bracket: continue
                    else: return False
                else:
                    return False
        if len(brackets_to_close) > 0:
            return False
        else:
            return True

brackets_in = "((((("
print(Solution().isValid(brackets_in))
