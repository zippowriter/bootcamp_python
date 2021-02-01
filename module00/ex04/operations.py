# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:31:52 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 01:31:56 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def calculator(a, b):
    Sum = a + b
    print('Sum:         ', Sum)
    Dif = a - b
    print('Difference:  ', Dif)
    Product = a * b
    print('Product:     ', Product)
    try:
        Quotient = a / b
        print('Quotient:    ', Quotient)
    except ZeroDivisionError:
        print('ERROR (div by zero)')
    try:
        Remainder = a % b
        print('Remainder:   ', Remainder)
    except ZeroDivisionError:
        print('ERROR (modulo by zero)')


try:
    args = sys.argv
    if len(args) != 3:
        raise ValueError
    a = int(args[1])
    b = int(args[2])
    calculator(a, b)
except ValueError:
    print('InputError: only numbers')
    print('')
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('\tpython operations.py 10 3')
