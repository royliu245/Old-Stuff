import random

def monty(k, strat = 'stay'):
    car = random.randint(1,k)
    pick = random.randint(1,k)

    if strat == 'switch':
        if car == pick:
            return "GOAT"
        else:
            return "CAR!"

    elif strat == 'stay':
        if car == pick:
            return "CAR!"
        else:
            return "GOAT"