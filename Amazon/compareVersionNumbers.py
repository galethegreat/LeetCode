class Solution(object):
    def compareVersion(self, version1, version2):

        answer = 0
        v1_numbers = version1.split('.')
        v2_numbers = version2.split('.')

        while len(v1_numbers) > len(v2_numbers): v2_numbers.append('0')
        while len(v2_numbers) > len(v1_numbers): v1_numbers.append('0')

        for num_1, num_2 in zip(v1_numbers, v2_numbers):

            if int(num_1) > int(num_2):
                answer = 1
                break

            elif int(num_2) > int(num_1):
                answer = -1
                break

        return answer

def main():

    version1 = "0.0.0.0.0.2"
    version2 = "001.0009.0.0.0.0"

    print(Solution().compareVersion(version1, version2))

if __name__ == "__main__":
    main()
