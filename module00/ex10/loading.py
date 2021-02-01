# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/01 21:37:54 by hkono             #+#    #+#              #
#    Updated: 2021/02/01 21:37:56 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time


def get_flag():
    global get_flag

    def get_flag():
        return False

    return True


def ft_progress(lst):
    if get_flag():
        bar_len = 20
        start = time.time()
        lst_len = len(lst)
    p = "\rETA: {:5.2f}s [ {:5.2f}%][{}] {}/{} | elapsed time {:5.2f}s"
    for val in lst:
        yield val
        val = int(val) + 1
        percent = val / lst_len * 100
        elapsed_time = time.time() - start
        ETA = lst_len * elapsed_time / val - elapsed_time
        n = bar_len / lst_len
        bar = "=" * int(val * n) + ">" + " " * (bar_len - int(val * n))
        print(p.format(ETA, percent, bar, val, lst_len, elapsed_time), end='')


def main():
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)


if __name__ == '__main__':
    main()
