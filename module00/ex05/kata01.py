# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 07:54:23 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 07:54:24 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for k in languages:
    print(f'{k} was created by {languages[k]}')
