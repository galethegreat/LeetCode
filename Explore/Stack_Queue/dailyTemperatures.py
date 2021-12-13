class Solution(object):
    def dailyTemperatures(self, temperatures):
        if len(temperatures) == 1:
            return [0]
        stack = list()
        answer = [0]*len(temperatures)
        for day, current_temperature in enumerate(temperatures):

            if len(stack) == 0 :
                stack.append((current_temperature,day))

            else:
                if stack[-1][0] < current_temperature:
                    temp = stack.pop()
                    while temp[0] < current_temperature:
                        answer[temp[1]] = day - temp[1]
                        if len(stack) > 0 :
                            temp = stack.pop()
                        else: break

                    if temp[0] >= current_temperature:
                        stack.append(temp)
                    stack.append((current_temperature,day))
                else:
                    stack.append((current_temperature,day))
        return answer

temperatures =  [30,60,90]
print(Solution().dailyTemperatures(temperatures))
