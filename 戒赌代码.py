money = 1000

while money > 0:
    bet = int(input())
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(a, b)
    if a + b == 7 or a + b == 11:
        print("玩家获胜！！！")
        money += bet
        print(money)
        
    elif a + b == 2 or a + b == 3 or a + b == 12:
        print("庄家获胜？？？")
        money -= bet
        print(money)

    else:
        while True:
            c = random.randint(1, 6)
            d = random.randint(1, 6)
            print(c, d)
            if c + d == 7:
                print('庄家获胜？？？')
                money -= bet
                print(money)
                break

            if c + d == a + b:
                print('玩家获胜！！！')
                money += bet
                print(money)
                break
if money == 0:
    print('赌吧老哥好！')
