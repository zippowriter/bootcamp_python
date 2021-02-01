# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:32:52 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 01:32:57 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def char_conver(new_str_list):
    lst = []
    for c in new_str_list:
        if c >= 'a' and c <= 'z':
            lst.append(c.upper())
        elif c >= 'A' and c <= 'Z':
            lst.append(c.lower())
        else:
            lst.append(c)
    return lst


arg_list = sys.argv
for arg in arg_list[1:]:
    new_str_list = list(arg)
    ans = char_conver(new_str_list)
    new_str = ''.join(list(reversed(ans)))
    print(new_str)
