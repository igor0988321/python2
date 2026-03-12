import random

def simulate_flips(flips):
    heads = 0
    tails = 0

    for i in range(flips):
        result = random.choice(['eagle', 'tail'])
        print(f'{i+1}. {result}')

        if result == 'eagle':
            heads +=1
        else:
            tails += 1

    return heads, tails

def flip_coin():
    print('Flipping coin...\n')

    flips = int(input('How many flips would you like to do? '))
    heads, tails = simulate_flips(flips)

    print(f'\nEagle: {heads} | Tails: {tails}')

flip_coin()