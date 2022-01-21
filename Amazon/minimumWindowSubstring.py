class Solution(object):
    def minWindow(self, s, t):
        def window_check(char_window,window_freq):
            for key,value in char_window.items():
                if window_freq.get(key, -1) >= value :continue
                else: return False
            return True

        if len(s) < len(t): return ""
        if len(s) == len(t) and len(s) == 1:
            if s == t: return s
            else: return ""

        t_freq = dict()
        s_freq = dict()
        chars_in_t = dict()

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        for key, value in t_freq.items():

            if s_freq.get(key, -1) < value:
                return ""
            else:
                chars_in_t[key] = value

        p1 = 0
        p2 = 0

        window_freq = dict()
        current_smallest_substring = ""
        len_window = None
        window_index = (p1, len(s))
        while p1 < len(s) and p2 < len(s):
            #print(f"{p1} {p2} {window_index}")
            if chars_in_t.get(s[p2], False):

                window_freq[s[p2]] = window_freq.get(s[p2], 0) + 1

                if window_check(chars_in_t, window_freq):

                    if len_window == None or p2-p1 < len_window:
                        len_window = p2-p1
                        window_index = (p1,p2+1)
                    #    if len_window == len(t): return s[p1:p2+1]
            #    print('Y')
                while window_check(chars_in_t,window_freq):

                    if chars_in_t.get(s[p1], False):

                        window_freq[s[p1]] = window_freq.get(s[p1], 0) - 1
                        if window_check(chars_in_t, window_freq):

                            if len_window == None or p2-p1 < len_window:
                                len_window = p2 - p1
                                window_index = (p1, p2+1)
                            #    if len_window == len(t): return s[p1:p2+1]

                        else:
                            window_freq[s[p1]] = window_freq.get(s[p1], 0) + 1
                            if len_window == None or p2-p1 < len_window:
                                len_window = p2 - p1
                                window_index = (p1, p2+1)
                            break
                    else:
                        if len_window == None or p2-p1 < len_window:
                            len_window = p2 - p1
                            window_index = (p1, p2+1)

                    p1 +=1
            p2 += 1

        return s[window_index[0]:window_index[1]]

def main():

    s = "cabwefgewcwaefgcf"

    t = "cae"
    print(Solution().minWindow(s, t))

if __name__ == "__main__":
    main()
