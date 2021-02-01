# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:32:09 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 01:32:12 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def text_analyzer(text=None, *args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if args:
        print('ERROR')
        return

    if text is not str:
        print('ERROR')
        return

    if text is None:
        print('What is the text to analyse?')
        text = input()

    print('The text contains {} characters:'.format(len(text)))

    def count_upper(text):
        count_u = 0
        for c in text:
            if c.isupper():
                count_u += 1
        return count_u
    print('- {} upper letters'.format(count_upper(text)))

    def count_low(text):
        count_l = 0
        for c in text:
            if c.islower():
                count_l += 1
        return count_l
    print('- {} lower letters'.format(count_low(text)))

    def count_punc(text):
        count_p = 0
        for c in text:
            if (c >= '!' and c <= '/') or (c >= ':' and c <= '@') or\
               (c >= '[' and c <= '`') or (c >= '{' and c <= '~'):
                count_p += 1
        return count_p
    print('- {} punctual marks'.format(count_punc(text)))

    def count_punc(text):
        count_s = 0
        for c in text:
            if c == ' ':
                count_s += 1
        return count_s
    print('- {} spaces'.format(count_punc(text)))
