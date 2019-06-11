import random


def guess_the_number_game():
    print('Lets play a game "guess that number"! Computer will generate random number and your task is to guess it.')
    num = random.randint(0, 100)
    guessed_number = int(input('Enter the number from 0 to 100: '))
    while guessed_number != num:

        if num > guessed_number:
            print('Pick higher number. Your was to low')
            guessed_number = int(input('Enter the number from 0 to 100: '))
        elif num < guessed_number:
            print('Pick lower number. Your was to high')
            guessed_number = int(input('Enter the number from 0 to 100: '))
        else:
            break

    print('You won! Your number was', num)


if __name__ == '__main__':
    guess_the_number_game()
