#O(nklogk)
class Solution(object):

    def groupAnagrams(self, strs):

        answer = dict()
        answer_list = list()

        for word in strs:

            word_sorted = "".join(sorted(word))

            if answer.get(word_sorted, False):
                answer[word_sorted].append(word)
            else:
                answer[word_sorted] = [word]

    #    for key,value in answer.items()
    #        answer_list.append(value)

        return answer.values()

def main():

    strs =["eat","tea","tan","ate","nat","bat"]

    print(Solution().groupAnagrams(strs))

if __name__ == "__main__":
    main()
