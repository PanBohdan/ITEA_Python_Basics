import random


def guess_the_number_game():
    print('Lets play a game "guess that number"! '
          'Computer will generate random number and your task is to guess it.')
    num = random.randint(0, 100)
    guessed_number = ''
    while guessed_number != num:
        guessed_number = input('Enter the number from 0 to 100: ')
        if guessed_number.isdigit():
            guessed_number = int(guessed_number)
            if num > guessed_number:
                print('Pick higher number. Your number was to low \n')

            elif num < guessed_number:
                print('Pick lower number. Your number was to high \n')

            else:
                break
        else:
            print('Error! Please try again. \n')
    print('You won! Your number was', num)


if __name__ == '__main__':
    guess_the_number_game()
