class Solution(object):
    def __init__(self):
        self.mem = dict()

    def climbStairs(self, n):
        def climb(current_step, n):

            if current_step > n:
                return 0
            if current_step == n:
                return 1

            if self.mem.get(current_step, False):
                return self.mem[current_step]

            self.mem[current_step] = climb(current_step + 1, n) + climb(current_step + 2, n)

            return self.mem[current_step]

        return climb(0, n)
        
def main():

    n = 6
    print(Solution().climbStairs(n))

if __name__ == '__main__':
    main()
