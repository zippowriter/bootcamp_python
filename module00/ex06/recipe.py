# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 09:13:34 by hkono             #+#    #+#              #
#    Updated: 2021/01/31 09:13:36 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sandwich_recipe = {
    'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
    'meal': 'lunch',
    'prep_time': '10',
}
cake_recipe = {
    'ingredients': ['flour', 'sugar', 'eggs'],
    'meal': 'dessert',
    'prep_time': '60',
}
salad_recipe = {
    'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
    'meal': 'lunch',
    'prep_time': '15',
}
cookbook = {
    'Sandwich': sandwich_recipe,
    'Cake': cake_recipe,
    'Salad': salad_recipe,
}


def add_recipe(cookbook, recipe):
    new_recipe = {}
    ingredients_list = []
    print('Please enter ingredients. If you finished, enter 0')
    while True:
        ans = input()
        if ans == '0':
            break
        ingredients_list.append(ans)
    print('Please enter meal.')
    meal = input()
    print('Please enter preparation time.')
    prep_time = input()
    new_recipe['ingredients'] = ingredients_list
    new_recipe['meal'] = meal
    new_recipe['prep_time'] = prep_time
    cookbook[recipe] = new_recipe


def delete_recipe(cookbook, recipe):
    try:
        cookbook.pop(recipe)
        print('done.')
        print('\n')
    except KeyError:
        print('{} is nothing in cookbook.'.format(recipe))
        print('\n')


def print_recipe(cookbook, recipe):
    try:
        cookbook[recipe]
        print('')
        print('Recipe for {}:'.format(recipe))
        print('Ingredients list: {}'.format(cookbook[recipe]['ingredients']))
        print('To be eaten for {}.'.format(cookbook[recipe]['meal']))
        print('Takes {} minutes of cooking.'.format(cookbook[recipe]['prep_time']))
        print('\n')
    except KeyError:
        print('{} is nothing in cookbook.'.format(recipe))
        print()


def print_cookbook(cookbook):
    print('Recipe names:')
    for k in cookbook:
        print('  ', k)
    print('\n')


def main():
    print('Please select an option by typing the corresponding number:')
    print('1: Add a recipe')
    print('2: Delete a recipe')
    print('3: Print a recipe')
    print('4: Print the cookbook')
    print('5: Quit')
    selected = input()
    if selected == '1':
        print('')
        print('Please enter the recipe\'s name to add.')
        recipe = input()
        print('')
        recipe = recipe.capitalize()
        add_recipe(cookbook, recipe)
    elif selected == '2':
        print('')
        print('Please enter the recipe\'s name to delete.')
        recipe = input()
        print('')
        recipe = recipe.capitalize()
        delete_recipe(cookbook, recipe)
    elif selected == '3':
        print('')
        print('Please enter the recipe\'s name to get its details:')
        recipe = input()
        print('')
        recipe = recipe.capitalize()
        print_recipe(cookbook, recipe)
    elif selected == '4':
        print('')
        print_cookbook(cookbook)
    elif selected == '5':
        print('')
        print('Cookbook closed.')
        sys.exit(0)
    else:
        print('This option does not exis, please type the corresponding number.')
        print('To exit, enter 5.')
        print('\n')


if __name__ == '__main__':
    while True:
        main()
