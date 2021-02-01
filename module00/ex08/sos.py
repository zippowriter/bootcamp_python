# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 20:46:37 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 20:46:39 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class EncodeMorse(object):
    def __init__(self):
        self.morse_code = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '--.-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            '.': '.-.-.-',
            ',': '--..--',
            ':': '---...',
            '?': '..--..',
            '_': '..--.-',
            '+': '.-.-.',
            '-': '-....-',
            '*': '-..-',
            '^': '......',
            '/': '-..-.',
            '@': '.--.-.',
            '(': '-.--.',
            ')': '-.--.-',
            '\"': '.-..-.',
            '\'': '.----.'
        }
        self.msg_lst = []
        self.morse_lst = []

    def error_check(self, messages):
        for i in range(len(messages)):
            for c in messages[i]:
                if c == ' ':
                    print('ERROR')
                    sys.exit(0)

    def to_upper(self, messages):
        for msg in messages:
            upper_msg = msg.upper()
            self.msg_lst.append(upper_msg)
        return self.msg_lst

    def encoding(self, msg_el):
        for key in msg_el:
            self.morse_lst.append(self.morse_code[key])
        morse = ''.join(self.morse_lst)
        return morse


def main():
    args = sys.argv
    msg_join = ' '.join(args[1:])
    messages = msg_join.split()
    em = EncodeMorse()
    em.error_check(messages)
    msg_up_lst = em.to_upper(messages)
    morse_lst = []
    for i in range(len(msg_up_lst)):
        morse_lst.append(em.encoding(msg_up_lst[i]))
    ans = ' / '.join(morse_lst)
    print(ans)


if __name__ == '__main__':
    main()
