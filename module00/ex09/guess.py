# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 22:14:58 by hkono             #+#    #+#              #
#    Updated: 2021/02/01 09:05:02 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random
import re


class GuessGame(object):

    def __init__(self):
        self.itr_num = 0
        pass

    def descript_game(self):
        print("This is an interactive guessing game!")
        print("You have to enter a number between 1 and 99", end='')
        print(" to find out the secret number.")
        print("Type 'exit' to end the game.")
        print("Good luck!")

    def game_system(self):
        answer = random.randint(1, 99)
        while True:
            self.itr_num += 1
            print("What\'s your guess betweenn 1 and 99?")
            num = input()
            if num == '42':
                print('The answer to the ultimate question of life, ', end='')
                print('the universe and everything is 42.')
                sys.exit(0)
            elif num == 'exit':
                print('Good bye!')
                sys.exit(0)
            if re.findall('[0-9]+', num) != [num]:
                print('That\'s not a number.')
                continue
            num = int(num)

            def high_or_low(answer, num):
                if num < answer:
                    print('Too low!')
                elif num > answer:
                    print('Too high!')
                else:
                    print('You won in {} attempts!'.format(self.itr_num))
                    sys.exit(0)
            high_or_low(answer, num)


def main():
    game = GuessGame()
    game.descript_game()
    game.game_system()


if __name__ == '__main__':
    main()
