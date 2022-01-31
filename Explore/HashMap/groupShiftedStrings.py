class Solution(object):

    def groupStrings(self, strings):
        hash = dict()
        for string_index, string in enumerate(strings):
            if len(string) == 1:
                hash.setdefault('_', []).append(string_index)
                continue

            diff_in_chars = list()
            for index in range(len(string)-1):
                diff = ord(string[index+1]) - ord(string[index])
                if diff < 0: diff += 26
                diff_in_chars.append(str(diff))
            prefix = f"{len(string)}_"
            val = "".join(diff_in_chars)
            key = prefix + val
            hash.setdefault(key, []).append(string_index)

        ans = list()
        for key,value in hash.items():
            ans.append([strings[val] for val in value])

        return ans

def main():
    strings =["abc","bcd","acef","xyz","az","ba","a","z","al"]
    print(Solution().groupStrings(strings))

if __name__ == "__main__":
    main()
