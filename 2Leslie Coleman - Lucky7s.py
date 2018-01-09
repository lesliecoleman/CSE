import random

def moneytaker(dice1,dice2,money,rounds):
    if money > 0:
        rounds +=1
        money -=1
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1+dice2 == 7
        