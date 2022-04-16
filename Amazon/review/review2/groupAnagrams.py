from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):

        anagrams = defaultdict(list)

        for index, word in enumerate(strs):

            letters = list(word)
            letters.sort()
            anagrams["".join(letters)].append(word)

        list_of_anagrams = [words for anagram, words in anagrams.items()]

        return list_of_anagrams



def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))

if __name__ == "__main__":
    main()
