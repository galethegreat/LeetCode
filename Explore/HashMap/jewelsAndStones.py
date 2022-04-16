class Solution(object):

    def numJewelsInStones(self, jewels, stones):
        jewls_set = set(jewels)
        number_of_jewels_in_stones = 0
        for stone in stones:
            if stone in jewls_set:
                number_of_jewels_in_stones += 1

        return number_of_jewels_in_stones


def main():

    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))

if __name__ == "__main__":
    main()
