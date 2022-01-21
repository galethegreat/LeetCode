def moneyChange(m):
    money = m
    coins = 0
    denominations = [10 ,5 ,1]
    for denomination in denominations:
        while money >= denomination:
            money -= denomination
            coins += 1
    return coins

def main():
    m = int(input())
    print(moneyChange(m))
if __name__ == "__main__":
    main()
