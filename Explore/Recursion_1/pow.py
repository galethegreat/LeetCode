class Solution(object):

    def fastPow(self, x, n):

        if n == 0: return 1
    
        half = self.fastPow(x , n // 2)
        result = half * half
        if n % 2 != 0: result *= x

        return result

    def myPow(self, x, n):
        if x == 0: return 0
        if n < 0: return 1/(self.fastPow(x, -n))
        return self.fastPow(x, n)

def main():
    x = 34.00515
    n = 3
    print(Solution().myPow(x,n))

if __name__ == '__main__':
    main()
