class Solution(object):
    def twoSum(self, numbers,target):

        length_of_numbers = len(numbers)
        first_index = 0
        last_index = length_of_numbers - 1

        while first_index < last_index:
            if numbers[first_index] + numbers[last_index] == target:
                break

            elif numbers[first_index] + numbers[last_index] > target:
                last_index -= 1

            else:
                first_index += 1


        return [first_index+1, last_index + 1]
#
 #[-3,-1,0,1, 8,9] = 7
 # 6, 8 , 7

def main():
    user_input = [-3,-1,0,1, 8,9]
    target = 7
    print(Solution().twoSum(user_input,target))
    #print(user_input)

if __name__ == "__main__":
    main()
