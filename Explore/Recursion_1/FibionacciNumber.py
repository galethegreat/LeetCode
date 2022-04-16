class Solution(object):
    def __init__(self):
        self.mem = dict()

    def fib(self, n):
        if self.mem.get(n, False): return self.mem[n]

        if n < 2:
            self.mem[n] = n
            return n

        self.mem[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.mem[n]

def main():

    n = 6
    print(Solution().fib(n))

if __name__ == '__main__':
    main()
