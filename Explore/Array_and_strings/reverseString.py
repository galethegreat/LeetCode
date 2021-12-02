class Solution(object):
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        #s.reverse() could just do this line lmao but practice 2 pointer

        first = 0
        last  = len(s) - 1

        while first < last:
            s[first], s[last] = s[last], s[first]
            first +=1
            last -= 1



def main():
    user_input = ["H","a"]
    Solution().reverseString(user_input)
    print(user_input)
if __name__ == "__main__":
    main()
