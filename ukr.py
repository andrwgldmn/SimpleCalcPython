#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Імпорт бібліотек
import math
import sympy
import sympy.abc
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy
import time

# Імпорт з бібліотек
from sympy import *
from math import sin, cos, tan
from os import *
from sympy.abc import symbols, x, y, theta

# Затримка перед очищенням
delay = 10  # час затримки в секундах;

# Для зберігання графіка в файл


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)

# Очищення екрана


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Початок
value = None
while value != 0:

    # Запит на вибір операцій
    print (' ----------------------------')
    value = int(input(" Оберіть категорію:: \n \n 0) Вихід \n 1) Прості дії \n 2) Тригонометрія \n 3) Геометрія \n 4) Інше \n 5) Вища математика \n 6) Електрика \n ---------------------------- \n "))
    # Вихід
    if (value == 0):
        print('-' * 28 + '\n Дякую за використання!\n' + '-' * 28)
    ##############################################################################################################################
    # Прості дії
    elif (value == 1):
        value = int(input(
            "\n 11) Додавання  \n 21) Віднімання \n 31) Ділення \n 41) Множення \n \n"))
        # Додавання
        if (value == 11):
            print ("")
            x = float(input(" Введіть перше число: "))
            print (' ----------------------------')
            y = float(input(" Введіть друге число: "))
            print (' ----------------------------')
            print (' {} + {}'.format(x, y))
            print (' ----------------------------')
            print (x + y)
            time.sleep(delay)
            cls()
        # Віднімання
        elif (value == 21):
            print ("")
            x = float(input(" Введіть перше число: "))
            print (' ----------------------------')
            y = float(input(" Введіть друге число: "))
            print (' ----------------------------')
            print (' {} - {}'.format(x, y))
            print (' ----------------------------')
            print (x - y)
            time.sleep(delay)
            cls()
        # Деление
        elif (value == 31):
            print ("")
            x = float(input(" Введіть перше число: "))
            print (' ----------------------------')
            y = float(input(" Введіть друге число: "))
            print (' ----------------------------')
            print (' {} / {}'.format(x, y))
            print (' ----------------------------')
            print (x / y)
            time.sleep(delay)
            cls()
        # Умножение
        elif (value == 41):
            print ("")
            x = float(input(" Введіть перше число: "))
            print (' ----------------------------')
            y = float(input(" Введіть друге число: "))
            print (' ----------------------------')
            print (' {} * {}'.format(x, y))
            print (' ----------------------------')
            print (x * y)
            time.sleep(delay)
            cls()
        else:
            print("Я не знаю що ви ввели, спробуйте ще раз.")
    ##############################################################################################################################
    # Тригонометрія
    elif (value == 2):
        value = int(input(
            "\n 12) Синус  \n 22) Косинус \n 32) Тангенс \n 42) Котангенс \n 52) Секанс \n 62) Косеканс \n \n"))
        # Знайти синус
        if (value == 12):
            print ("")
            x = float(input(" Введіть число: "))
            print (' ----------------------------')
            print (sin(x))
            time.sleep(delay)
            cls()
        # Знайти косинус
        elif (value == 22):
            print ("")
            x = float(input(" Введіть число: "))
            print (' ----------------------------')
            print (cos(x))
            time.sleep(delay)
            cls()
        # Знайти тангенс
        elif (value == 32):
            print ("")
            x = float(input(" Введіть число: "))
            print (' ----------------------------')
            print (tan(x))
            time.sleep(delay)
            cls()
        # Знайти котангенс
        elif (value == 42):
            print ("")
            x = float(input(" Введіть число: "))
            tan = tan(x)
            print (' ----------------------------')
            print (1 / tan)
            time.sleep(delay)
            cls()
        # Знайти секанс
        elif (value == 52):
            print ("")
            x = float(input(" Введіть число: "))
            sin = sin(x)
            print (' ----------------------------')
            print (1 / sin)
            time.sleep(delay)
            cls()
        # Знайти косеканс
        elif (value == 62):
            print ("")
            x = float(input(" Введіть число: "))
            cos = cos(x)
            print (' ----------------------------')
            print (1 / cos)
            time.sleep(delay)
            cls()
        else:
            print("Я не знаю що ви ввели, спробуйте ще раз.")
    ##############################################################################################################################
    # Геометрія
    elif (value == 3):
        value = int(input("\n 13) Знайти гіпотенузу  \n 23) Знайти катет \n 33) Знайти площу прямокутника \n 43) Знайти площу трикутника \n 53) Знайти площу прямокутного трикутника \n 63) Знайти площу рівностороннього трикутника \n 73) Знайти площу ромба \n 83) Знайти площу паралелограма \n 93) Знайти площу трапеції \n \n"))
        # Знайти гіпотенузу
        if (value == 13):
            print ("")
            katet_one = float(input(" Введіть перший катет: "))
            katet_two = float(input(" Введіть другий катет: "))
            gipot = math.sqrt(katet_one**2 + katet_two**2)
            print ("")
            print (gipot)
            time.sleep(delay)
            cls()
        # Знайти катет
        elif (value == 23):
            print ("")
            katet = float(input(" Введіть відомий катет: "))
            gipot = float(input(" Введіть гіпотенузу: "))
            res = math.sqrt(gipot**2 - katet**2)
            print ("")
            print (res)
            time.sleep(delay)
            cls()
        # Знайти площу прямокутника
        elif (value == 33):
            print ("")
            one = float(input(" Введіть сторону: "))
            two = float(input(" Введіть сторону: "))
            print ("")
            print (two * one)
            time.sleep(delay)
            cls()
        # Знайти площу трикутника
        elif (value == 43):
            print ("")
            one = float(input(" Введіть сторону: "))
            two = float(input(" Введіть висоту: "))
            print ("")
            print ((one * two) * 0.5)
            time.sleep(delay)
            cls()
        # Знайти площу прямокутного трикутника
        elif (value == 53):
            print ("")
            one = float(input(" Введіть 1 сторону: "))
            two = float(input(" Введіть 2 сторону: "))
            print ("")
            print ((one * two) / 2)
            time.sleep(delay)
            cls()
        # Знайти площу рівностороннього трикутника
        elif (value == 63):
            print ("")
            three = 3
            one = float(input(" Введіть сторону: "))
            print ("")
            print ((one * math.sqrt(three)) / 4)
            time.sleep(delay)
            cls()
        # Знайти площу ромба
        elif (value == 73):
            print ("")
            one = float(input(" Введіть сторону: "))
            vis = float(input(" Введіть висоту: "))
            print ("")
            print (one * vis)
            time.sleep(delay)
            cls()
        # Знайти площу паралелограма
        elif (value == 83):
            print ("")
            one = float(input(" Введіть 1 сторону: "))
            two = float(input(" Введіть 2 сторону: "))
            sine = float(input(" Введіть кут: "))
            print ("")
            print (one * two * math.sin(sine))
            time.sleep(delay)
            cls()
        # Знайти площу трапеції
        elif (value == 93):
            print ("")
            one = float(input(" Введіть 1 сторону: "))
            two = float(input(" Введіть 2 сторону: "))
            vis = float(input(" Введіть висоту: "))
            print ("")
            print (((one + two) / 2) * vis)
            time.sleep(delay)
            cls()
        else:
            print("Я не знаю що ви ввели, спробуйте ще раз.")
    ##############################################################################################################################
    # Інше
    elif (value == 4):
        value = int(
            input("\n 14) Побудувати графік  \n 24) Зпростити вираз \n \n "))
        # Будуємо графік
        if (value == 14):
            fig = plt.figure()
            # Тип графіка
            ax = fig.add_subplot(111)
            rect = ax.patch
            rect.set_facecolor('white')
            rect.set_alpha(0)
            print("")
            # Ліміт по х
            x = np.arange(-25, 25)
            # Введення виразу
            y = input(" Введіть вираз: ")
            plt.plot(x, y)
            ax = plt.gca()
            ax.plot(x, y, 'black')
            xax = ax.xaxis
            xlocs = xax.get_ticklocs()
            xlabels = xax.get_ticklabels()
            xlines = xax.get_ticklines()
            ax.grid(True, which='major', color='y',
                    linewidth=2., linestyle='solid')
            ax.grid(True, which='minor', color='k')
            for label in ax.xaxis.get_ticklabels():
                label.set_color('black')
                label.set_rotation(0)
                label.set_fontsize(14)
            for line in ax.yaxis.get_ticklines():
                line.set_color('black')
                line.set_markersize(14)
                line.set_markeredgewidth(3)
            # Зберігання у файл
            save('graphic', fmt='png')
            for label in xlabels:
                label.set_color('black')
                label.set_rotation(0)
                label.set_fontsize(12)
            # Показ графіка
            plt.show()
            # Зпростити вираз
        elif (value == 24):
            print ("")
            primer = raw_input(" Введіть приклад: ")
            res = simplify(primer)
            print ("")
            sympy.pprint(res)
            time.sleep(delay)
            cls()
        else:
            print("Я не знаю що ви ввели, спробуйте ще раз.")
    ##############################################################################################################################
    # Вища математика
    elif (value == 5):
        value = int(input("\n 15) Похідна  \n 25) Інтеграл \n 35) Ліміт (x->оо) \n 45) Ліміт (x->0) \n 55) Ліміт (x->1) \n 65) Ліміт (будь-яке число) \n 75) Визначений інтеграл \n \n "))
        # Похідна
        if (value == 15):
            print ("")
            input_string = raw_input(' Вираз: ')
            print ("")
            res = sum(sympy.diff(input_string, var) for var in [x, y])
            sympy.pprint(res)
            time.sleep(delay)
            cls()
        # Інтеграл
        elif (value == 25):
            print ("")
            x = Symbol("x")
            y = Symbol("y")
            input_string = input(' Вираз: ')
            print ("")
            sympy.pprint(sympy.Integral(input_string, x))
            print ("")
            sympy.pprint(integrate(input_string, x))
            time.sleep(delay)
            cls()
        # Визначений інтеграл
        elif (value == 75):
            print ("")
            x = Symbol("x")
            y = Symbol("y")
            input_string = input(' Вираз: ')
            ot = float(input(' Від: '))
            do = float(input(' До: '))
            print ("")
            sympy.pprint(sympy.Integral(input_string, (x, ot, do)))
            print ("")
            sympy.pprint(integrate(input_string, (x, ot, do)))
            time.sleep(delay)
            cls()
        # Лимит (x->оо)
        elif (value == 35):
            print ("")
            value = input(' Вираз: ')
            print ("")
            sympy.pprint(limit(value, x, oo))
            time.sleep(delay)
            cls()
        # Лимит (x->0)
        elif (value == 45):
            print ("")
            value = input(' Вираз: ')
            print ("")
            sympy.pprint(limit(value, x, 0))
            time.sleep(delay)
            cls()
        # Лимит (x->1)
        elif (value == 55):
            print ("")
            value = input(' Вираз: ')
            print ("")
            sympy.pprint(limit(value, x, 1))
            time.sleep(delay)
            cls()
        # Лимит (любое число)
        elif (value == 65):
            print ("")
            value = input(' Вираз: ')
            stremlenie = input(' До чого прямує "x"? ')
            print ("")
            sympy.pprint(limit(value, x, stremlenie))
            time.sleep(delay)
            cls()
        else:
            print("Я не знаю що ви ввели, спробуйте ще раз.")
    ################################################################################################################################
    elif (value == 6):
        value = int(input(
            "\n 16) Активний опір  \n 26) Індуктивний опір \n 36) Ємнісний опір \n 46) Потужність \n 56) Струм \n 66) Напруга \n \n "))
        # Активний опір
        if (value == 16):
            print ("")
            u = float(input(" Напруга: "))
            print (' ----------------------------')
            i = float(input(" Струм: "))
            print ("")
            print (u / i)
            time.sleep(delay)
            cls()
        # Індуктивний опір
        elif (value == 26):
            print ("")
            l = float(input(" Індуктивність: "))
            print (' ----------------------------')
            f = float(input(" Частота: "))
            print ("")
            print (2 * math.pi * f * l)
            time.sleep(delay)
            cls()
        # Ємнісний опір
        elif (value == 36):
            print ("")
            c = float(input(" Ємність: "))
            print (' ----------------------------')
            f = float(input(" Частота: "))
            print ("")
            print (1 / (2 * math.pi * f * c))
            time.sleep(delay)
            cls()
        # Потужність
        elif (value == 46):
            print ("")
            u = float(input(" Напруга: "))
            print (' ----------------------------')
            i = float(input(" Струм: "))
            print ("")
            print (u * i)
            time.sleep(delay)
            cls()
        # Струм
        elif (value == 56):
            print ("")
            u = float(input(" Напруга: "))
            print (' ----------------------------')
            r = float(input(" Опір: "))
            print ("")
            print (u / r)
            time.sleep(delay)
            cls()
        # Напруга
        elif (value == 66):
            print ("")
            r = float(input(" Опір: "))
            print (' ----------------------------')
            i = float(input(" Струм: "))
            print ("")
            print (r * i)
            time.sleep(delay)
            cls()
        else:
            print("Я не знаю що ви ввели, спробуйте ще раз.")
    else:
        print("Я не знаю що ви ввели, спробуйте ще раз.")
