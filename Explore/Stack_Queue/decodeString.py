import re

class Solution:
    def galeRe(self,s):

        stack = list()
        for index,char in enumerate(s):
            if char == '[':
                stack.append(']')
            elif char == ']':
                stack.pop()
            if len(stack) == 0:
                return index

    def decodeString(self, s: str) -> str:
        pattern = re.search("[0-9+]\[(.*)\]",s)
        start = s.find('[')
        if start != -1:
            k =  re.findall("([0-9]+)\[",s[:start+1])
            end = self.galeRe(s[start:]) + start
            index_1 = s.find(k[0])
            first_part = s[:index_1]
            second_part = s[start+1:end]
            third_part = s[end+1:]
            return first_part + int(k[0])*self.decodeString(second_part) + self.decodeString(third_part)

        else:
            return s

s2 = "2[abc]3[cd]ef"
s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))
