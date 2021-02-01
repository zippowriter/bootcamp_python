# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:32:33 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 01:32:35 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def EvenOrOdd(num):
    if num / 2 == 0:
        print('I\'m Even.')
    else:
        print('I\'m Odd')
    return


try:
    lst = sys.argv
    if len(lst) > 2:
        raise IndexError('ERROR')
    num = int(lst[1])
    EvenOrOdd(num)
except ValueError:
    print('ERROR')
except IndexError:
    print('ERROR')
