class Solution:
    def evalRPN(self, tokens):
        def evaluate(temp1,temp2,token):
            if token == '+':
                return temp1 + temp2
            elif token == '-':
                return temp2 - temp1
            elif token == '*':
                return temp1 * temp2
            elif token == '/':
                return int(temp2 / temp1)

        if len(tokens) == 1:
            return tokens[0]

        answer = None
        operations = ['+','-','*','/']
        operations = set(operations)

        stack = list()

        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                answer = evaluate(int(temp1), int(temp2), token)
                stack.append(answer)

        return answer

tokens =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))
