#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Импорт библиотек
import math, sympy, sympy.abc, numpy as np, matplotlib, sys, matplotlib.pyplot as plt, os, scipy, time

#Импорт из библиотек
from sympy import *
from math import sin, cos, tan
from sys import *
from os import *
from sympy.abc import symbols, x, y, theta

#Задержка перед очисткой
delay = 10            #время задержки в секундах;

#Для сохранения графика в файл
def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)

#Чистка экрана
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Начало
start = 1
while start:
    start = 0

#Запрос на выбор операций
    print (' ----------------------------')
    value = int(input(" Выберите категорию: \n \n 0) Выход \n 1) Простые действия \n 2) Тригонометричекие функции \n 3) Геометрия \n 4) Прочее \n 5) Высшая математика \n 6) Электрика \n ---------------------------- \n "  ))
    #Выход
    if (value == 0):
        print( '-' * 28 + '\n Спасибо за использование!\n' +  '-' * 28)
        sys.exit()
    ##############################################################################################################################
    #Простые действия
    if (value == 1):
        value = int(input("\n 11) Сложение  \n 21) Вычитание \n 31) Деление \n 41) Умножение \n \n"))
        #Сложение
        if (value == 11):
            print ("")
            x = float(input(" Введите первое число: "))
            print (' ----------------------------')
            y = float(input(" Введите второе число: "))
            print (' ----------------------------')
            print (' {} + {}'.format(x, y)) 
            print (' ----------------------------')    
            print ( x + y )
            time.sleep(delay)
            cls()
            start = 1
        #Вычитание
        if (value == 21):
            print ("")
            x = float(input(" Введите первое число: "))
            print (' ----------------------------')
            y = float(input(" Введите второе число: "))
            print (' ----------------------------')
            print (' {} - {}'.format(x, y))   
            print (' ----------------------------')    
            print ( x - y )
            time.sleep(delay)
            cls()
            start = 1
        #Деление
        if (value == 31):
            print ("")
            x = float(input(" Введите первое число: "))
            print (' ----------------------------')
            y = float(input(" Введите второе число: "))
            print (' ----------------------------')
            print (' {} / {}'.format(x, y))
            print (' ----------------------------')
            print float( x / y )
            time.sleep(delay)
            cls()
            start = 1
        #Умножение
        if (value == 41):
            print ("")
            x = float(input(" Введите первое число: "))
            print (' ----------------------------')
            y = float(input(" Введите второе число: "))
            print (' ----------------------------')
            print (' {} * {}'.format(x, y))
            print (' ----------------------------')
            print ( x * y )
            time.sleep(delay)
            cls()
            start = 1
        else:
            start = 1
    ##############################################################################################################################
    #Тригонометрические функции
    if (value == 2):
        value = int(input("\n 12) Синус  \n 22) Косинус \n 32) Тангенс \n 42) Котангенс \n 52) Секанс \n 62) Косеканс \n \n"))
        #Найти синус
        if (value == 12):
            print ("")
            x = float(input(" Введите число: "))
            print (' ----------------------------')
            print float( sin(x) )
            time.sleep(delay)
            cls()
            start = 1
        #Найти косинус
        if (value == 22):
            print ("")
            x = float(input(" Введите число: "))
            print (' ----------------------------')
            print float( cos(x) )
            time.sleep(delay)
            cls()
            start = 1
        #Найти тангенс
        if (value == 32):
            print ("")
            x = float(input(" Введите число: "))
            print (' ----------------------------')
            print float( tan(x) )
            time.sleep(delay)
            cls()
            start = 1
        #Найти котангенс
        if (value == 42):
            print ("")
            x = float(input(" Введите число: "))
            tan = tan(x)
            print (' ----------------------------')
            print float( 1/tan )
            time.sleep(delay)
            cls()
            start = 1
        #Найти секанс
        if (value == 52):
            print ("")
            x = float(input(" Введите число: "))
            sin = sin(x)
            print (' ----------------------------')
            print float( 1/sin )
            time.sleep(delay)
            cls()
            start = 1
        #Найти косеканс
        if (value == 62):
            print ("")
            x = float(input(" Введите число: "))
            cos = cos(x)
            print (' ----------------------------')
            print float( 1/cos )
            time.sleep(delay)
            cls()
            start = 1
        else:
            start = 1
    ##############################################################################################################################
    #Геометрия
    if (value == 3):
        value = int(input("\n 13) Найти гипотенузу  \n 23) Найти катет \n 33) Найти площадь прямоугольника \n 43) Найти площадь треугольника \n 53) Найти площадь прямоугольного треугольника \n 63) Найти площадь равностороннего треугольника \n 73) Найти площадь ромба \n 83) Найти площадь паралелограма \n 93) Найти площадь трапеции \n \n"))
        #Найти гипотенузу
        if (value == 13):
            print ("")
            katet_one = float(input(" Введите первый катет: "))
            katet_two = float(input(" Введите второй катет: "))
            gipot = math.sqrt(katet_one**2 + katet_two**2)
            print ("")
            print (gipot)
            time.sleep(delay)
            cls()
            start = 1
        #Найти катет
        if (value == 23):
            print ("")
            katet = float(input(" Введите известный катет: "))
            gipot = float(input(" Введите гипотенузу: "))
            res = math.sqrt(gipot**2 - katet**2)
            print ("")
            print (res)
            time.sleep(delay)
            cls()
            start = 1
        #Найти площадь прямоугольника
        if (value == 33):
            print ("")
            one = float(input(" Введите сторону: "))
            two = float(input(" Введите сторону: ")) 
            print ("")
            print (two * one)
            time.sleep(delay)
            cls()
            start = 1
        #Найти площадь треугольника
        if (value == 43):
            print ("")
            one = float(input(" Введите сторону: "))
            two = float(input(" Введите высоту: ")) 
            print ("")
            print ((one*two)*0.5)
            time.sleep(delay)
            cls()
            start = 1
        #Найти площадь прямоугольного треугольника
        if (value == 53):
            print ("")
            one = float(input(" Введите 1 сторону: "))
            two = float(input(" Введите 2 сторону: ")) 
            print ("")
            print ((one*two)/2)
            time.sleep(delay)
            cls()
            start = 1
        #Найти площадь равностороннего треугольника
        if (value == 63):
            print ("")
            three = 3
            one = float(input(" Введите сторону: "))
            print ("")
            print ((one*math.sqrt(three))/4)
            time.sleep(delay)
            cls()
            start = 1
        #Найти площадь ромба
        if (value == 73):
            print ("")
            one = float(input(" Введите сторону: "))
            vis = float(input(" Введите высоту: "))
            print ("")
            print (one * vis)
            time.sleep(delay)
            cls()
            start = 1
        #Найти площадь паралеллограма
        if (value == 83):
            print ("")
            one = float(input(" Введите 1 сторону: "))
            two = float(input(" Введите 2 сторону: "))
            sine = float(input(" Введите угол: "))
            print ("")
            print (one * two * math.sin(sine))
            time.sleep(delay)
            cls()
            start = 1
        #Найти площадь трапеции
        if (value == 93):
            print ("")
            one = float(input(" Введите 1 сторону: "))
            two = float(input(" Введите 2 сторону: "))
            vis = float(input(" Введите высоту: "))
            print ("")
            print (((one + two)/2)*vis)
            time.sleep(delay)
            cls()
            start = 1
        else:
            start = 1
    ##############################################################################################################################
    #Прочее
    if (value == 4):
        value = int(input("\n 14) Построить график  \n 24) Сократить пример \n \n "))
        #Строим график
        if (value == 14):
            fig = plt.figure()
            #Тип графика
            ax = fig.add_subplot(111)
            rect = ax.patch
            rect.set_facecolor('white')
            rect.set_alpha(0)
            print("")
            #Предел по х
            x = np.arange(-25, 25)
            #Ввод примера
            y = input(" Введите выражение: ")
            plt.plot(x, y)
            ax = plt.gca()
            ax.plot(x, y, 'black')
            xax = ax.xaxis
            xlocs = xax.get_ticklocs()
            xlabels = xax.get_ticklabels()
            xlines = xax.get_ticklines()
            # вспомогательная сетка для главных делений 
            ax.grid(True, which='major', color='y', linewidth=2., linestyle='solid')
            # вспомогательная сетка для вспомогательных делений 
            ax.grid(True, which='minor', color='k')
            # Ось абсцисс
            for label in ax.xaxis.get_ticklabels():
                # label - это экземпляр текста Text
                label.set_color('black')
                label.set_rotation(0)
                label.set_fontsize(14)
            # Ось ординат
            for line in ax.yaxis.get_ticklines():
                # line - это экземпляр плоской линии Line2D
                line.set_color('black')   # задаём цвет линии деления
                line.set_markersize(14)   # задаём длину линии деления
                line.set_markeredgewidth(3)   # задаём толщину линии деления
            #Сохранение в файл
            save('graphic', fmt='png')
            for label in xlabels:
                # цвет подписи деленений оси OX
                label.set_color('black')
                # поворот подписей деленений оси OX 
                label.set_rotation(0)
                # размер шрифта подписей делений оси OX 
                label.set_fontsize(12)
            #Вывод графика
            plt.show()
            start = 1
        else:
            start = 1
            #Сократить пример
            if (value == 24):
                print ("")
                primer = raw_input(" Введите пример: ")
                res = simplify(primer)
                print ("")
                sympy.pprint (res)
                time.sleep(delay)
                cls()
                start = 1
            else:
                start = 1
    ##############################################################################################################################
    #Высшая математика
    if (value == 5):
        value = int(input("\n 15) Производная  \n 25) Интеграл \n 35) Лимит (x->оо) \n 45) Лимит (x->0) \n 55) Лимит (x->1) \n 65) Лимит (любое число) \n 75) Определённый интеграл \n \n "))
        #Производная
        if (value == 15):
            print ("")
            input_string = raw_input(' Выражение: ')
            print ("")
            res = sum(sympy.diff(input_string, var) for var in [x,y])
            sympy.pprint (res)
            time.sleep(delay)
            cls()
            start = 1
        #Интеграл
        if (value == 25):
            print ("")
            input_string = raw_input(' Выражение: ')
            print ("")
            sympy.pprint (sympy.Integral(input_string, x))
            print ("")
            sympy.pprint (integrate(input_string, x))
            time.sleep(delay)
            cls()
            start = 1
        #Определённый интеграл
        if (value == 75):
            print ("")
            input_string = raw_input(' Выражение: ')
            ot = float(input(' От: '))
            do = float(input(' До: '))
            print ("")
            sympy.pprint (sympy.Integral(input_string, (x, ot, do)))
            print ("")
            sympy.pprint (integrate(input_string, (x, ot, do)))
            time.sleep(delay)
            cls()
            start = 1
        #Лимит (x->оо)
        if (value == 35 ):
            print ("")
            value = input(' Выражение: ') 
            print ("")
            sympy.pprint (limit(value, x, oo))
            time.sleep(delay)
            cls()
            start = 1
        #Лимит (x->0)
        if (value == 45 ):
            print ("")
            value = input(' Выражение: ') 
            print ("")
            sympy.pprint (limit(value, x, 0))
            time.sleep(delay)
            cls()
            start = 1
        #Лимит (x->1)
        if (value == 55 ):
            print ("")
            value = input(' Выражение: ') 
            print ("")
            sympy.pprint (limit(value, x, 1))
            time.sleep(delay)
            cls()
            start = 1
        #Лимит (любое число)
        if (value == 65 ):
            print ("")
            value = input(' Выражение: ') 
            stremlenie = input(' К чему стремится "x"? ')
            print ("")
            sympy.pprint (limit(value, x, stremlenie))
            time.sleep(delay)
            cls()
            start = 1 
        else:
            start = 1
    ################################################################################################################################
    if (value == 6):
        value = int(input("\n 16) Активное сопротивление  \n 26) Индуктивное сопротивление \n 36) Ёмкостное сопротивление \n 46) Мощность \n 56) Ток \n 66) Напряжение \n \n "))
        #Активное сопротивление
        if (value == 16):
            print ("")
            u = float(input(" Напряжение: "))
            print (' ----------------------------')
            i = float(input(" Ток: "))  
            print ("")
            print ( u/i )
            time.sleep(delay)
            cls()
            start = 1 
        #Индуктивное сопротивление
        if (value == 26):
            print ("")
            l = float(input(" Индуктивность: "))
            print (' ----------------------------')
            f = float(input(" Частота: "))  
            print ("")
            print ( 2*math.pi*f*l )
            time.sleep(delay)
            cls()
            start = 1 
        #Ёмкостное сопротивление
        if (value == 36):
            print ("")
            c = float(input(" Ёмкость: "))
            print (' ----------------------------')
            f = float(input(" Частота: ")) 
            print ("") 
            print ( 1/(2*math.pi*f*c) )
            time.sleep(delay)
            cls()
            start = 1
        #Мощность
        if (value == 46):
            print ("")
            u = float(input(" Напряжение: "))
            print (' ----------------------------')
            i = float(input(" Ток: ")) 
            print ("") 
            print ( u*i )
            time.sleep(delay)
            cls()
            start = 1 
        #Ток
        if (value == 56):
            print ("")
            u = float(input(" Напряжение: "))
            print (' ----------------------------')
            r = float(input(" Сопротивление: ")) 
            print ("") 
            print ( u/r )
            time.sleep(delay)
            cls()
            start = 1 
        #Напряжение
        if (value == 66):
            print ("")
            r = float(input(" Сопротивление: "))
            print (' ----------------------------')
            i = float(input(" Ток: ")) 
            print ("") 
            print ( r*i )
            time.sleep(delay)
            cls()
            start = 1 
    else:
       start = 1
