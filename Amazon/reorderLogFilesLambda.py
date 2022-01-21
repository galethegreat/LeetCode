class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        # will do loop thorugh the list of logs and separate letter logs and digit logs to dfifferent lists so at the eand after sorting letter logs we can return combined lists

        for log in logs:
            if log.split(' ')[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        # after seperating logs to different lists we sort letter logs
        # whatever comes first in lambada function it sorts by that parametr if second parametr is given it checks if first parametr is same ans sorts by given second parametr in lambda fucntion

        letter_logs.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))
        return letter_logs + digit_logs
