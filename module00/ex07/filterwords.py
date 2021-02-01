# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 18:25:20 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 18:25:22 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re


def filter_words(args):
    word_lst = [word for word in args[1].split(' ')]
    ans_lst = [ans for ans in word_lst if len(ans) >= int(args[-1])]
    print(ans_lst)


def error_checker(args):

    def arglen_check(args):
        if len(args) > 3:
            return 0
        return 1

    def argnum_check(args):
        if len(re.findall('[0-9]+', args[-1])) == 0:
            return 0
        return 1

    def str_check(args):

        if re.findall('[0-9]+', args[1])[0] == args[1]:
            return 0
        return 1

    try:
        if arglen_check(args) == 0:
            raise ValueError
        elif argnum_check(args) == 0:
            raise ValueError
        elif str_check(args) == 0:
            raise ValueError
    except ValueError:
        print('ERROR')
        sys.exit(0)


def main():
    args = sys.argv
    error_checker(args)
    filter_words(args)
    return


if __name__ == '__main__':
    main()
