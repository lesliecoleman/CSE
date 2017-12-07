import random
player_money = 15
player_input = input("So I see your feeling lucky...have fun...loser. Go ahead and roll.")
rolls = 0

while player_money != 0:
    rolls += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    player_roll = dice1 + dice2
    print(player_roll)
    if player_roll == 7:
        player_money += 5
        print("Guess you were lucky. Guess you have %s dollars now... loser" % player_money)
        print("You've rolled %s times" % rolls)
        print("Roll again...soon I'll take all your money...loser")
    else:
        player_money -= 1
        print("Guess you weren't lucky today. You now have %s dollars" % player_money)
        print("You've rolled %s times" % rolls)
        input("Wanna Try Again?")
if player_money == 0:
    print("HA! I got all your money...loser. You took %s tries to lose all your money...loser" % rolls)