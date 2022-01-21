
#O(nlognklogk)
class Solution(object):

    def groupAnagrams(self, strs):

        strs_copy = list()
        for index, word in enumerate(strs):
            strs_copy.append(("".join(sorted(word)), index))

        strs_copy.sort()


        answer = list()
        answer_list = list()
        while len(strs_copy) > 0:

            last_anagram = strs_copy.pop()
            answer.append(strs[last_anagram[1]])
            str_compare = last_anagram[0]

            while len(strs_copy) > 0 and strs_copy[-1][0] == str_compare:
                answer.append(strs[strs_copy.pop()[1]])


            answer_list.append(answer)
            answer = list()

        return answer_list

def main():

    strs =["eat","tea","tan","ate","nat","bat"]

    print(Solution().groupAnagrams(strs))

if __name__ == "__main__":
    main()
