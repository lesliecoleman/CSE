import random


def money_taker(dice1, dice2, money, rounds, highest_round, highest_money):
    if money > 0:
        if highest_money < money:
            highest_money = money
            highest_round = rounds
        rounds += 1
        money -= 1
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1+dice2 == 7:
            money += 5
            print("You got a 7. You have played %d times. You now have $%d" % (rounds, money))
            money_taker(dice1, dice2, money, rounds, highest_round, highest_money)
        elif dice1+dice2 != 7:
            print("The number was %d. You have played %d times. You now have $%d" % (dice1 + dice2, rounds, money))
            money_taker(dice1, dice2, money, rounds, highest_round, highest_money)
    else: print("Why you no have money. Only took you %d rounds. "
                "Your highest amount of money was $%d at round %d" % (rounds, highest_money, highest_round))


money_taker(0,0,15,0,0,0)