from collections import Counter

class Solution(object):
    def minWindow(self, s, t):

        if len(s) < len(t): return ""
        if len(s) == len(t) and len(s) == 1:
            if s == t: return s
            else: return ""

        chars_freq_in_t = Counter(t)

        p1, p2 = 0,0

        unique_chars = set()

        smallest_window = float('inf')
        smallest_window_index = None

        window_freq = dict()
        required_number_of_conditions = len(chars_freq_in_t)

        while p2 < len(s):
            if s[p2] in chars_freq_in_t:
                window_freq[s[p2]] = window_freq.get(s[p2], 0) + 1

                if window_freq[s[p2]] >= chars_freq_in_t[s[p2]] :
                    unique_chars.add(s[p2])

                if len(unique_chars) == required_number_of_conditions:
                    current_window = p2 - p1

                    if current_window < smallest_window:
                        smallest_window = current_window
                        smallest_window_index = (p1,p2+1)
                        
                while len(unique_chars) == required_number_of_conditions and p1 <= p2:
                    if s[p1] in chars_freq_in_t:
                        window_freq[s[p1]] = window_freq.get(s[p1], 0) - 1

                        if  window_freq[s[p1]] < chars_freq_in_t[s[p1]]:
                            unique_chars.remove(s[p1])

                        if len(unique_chars) != required_number_of_conditions:
                            window_freq[s[p1]] = window_freq.get(s[p1], 0) + 1
                            current_window = p2 - p1
                            if current_window < smallest_window:
                                smallest_window = current_window
                                smallest_window_index = (p1,p2+1)
                            break

                    current_window = p2 - p1
                    if current_window < smallest_window:
                        smallest_window = current_window
                        smallest_window_index = (p1,p2+1)

                    p1 += 1
            p2 += 1

        if smallest_window_index is None: return ""

        return s[smallest_window_index[0]:smallest_window_index[1]]

def main():

    s = "ab"
    t = "A"

    print(Solution().minWindow(s, t))

if __name__ == "__main__":
    main()
