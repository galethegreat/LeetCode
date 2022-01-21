class Solution(object):
    def reorderLogFiles(self, logs):
        digit_logs = list()
        letter_logs = list()

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)

            else:
                letter_logs.append(log)

        letter_logs_touple = list()
        for index, log in enumerate(letter_logs):
            id  = log.split()[0]
            content = log.split()[1:]
            letter_logs_touple.append((content,id,index))

        letter_logs_touple.sort()
        letter_logs_sorted = [0] * len(letter_logs_touple)

        for index, log in enumerate(letter_logs_touple):
            letter_logs_sorted[index] = letter_logs[log[2]]

        return letter_logs_sorted + digit_logs

logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]

x = Solution().reorderLogFiles(logs)
print(x)
