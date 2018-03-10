#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Импорт библиотек
import math, sympy, sympy.abc, numpy as np, matplotlib, sys, matplotlib.pyplot as plt, os, scipy

#Импорт из библиотек
from sympy import *
from math import sin, cos, tan, acos, asin, atan
from sys import *
from os import *
from sympy.abc import symbols

#Для сохранения графика в файл
def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)

#Начало
start = 1
while start:
    start = 0

#Запрос на выбор операций
    print (' ----------------------------')
    value = int(input(" Выберите нужное действие: \n \n 0) Выход \n 1) Сложение  \n 2) Вычитание \n 3) Деление \n 4) Умножение \n 5) Найти синус \n 6) Найти косинус \n 7) Найти тангенс \n 8) Найти котангенс \n 9) Построить график  \n 10) Найти производную \n ---------------------------- \n "))

    #Выход
    if (value == 0):
        print( '-' * 28 + '\n Спасибо за использование!\n' +  '-' * 28)
        sys.exit()

    #Сложение
    if (value == 1):
        x = float(input(" Введите первое число: "))
        print (' ----------------------------')
        y = float(input(" Введите второе число: "))
        print (' ----------------------------')
        print (' {} + {}'.format(x, y)) 
        print (' ----------------------------')    
        print ( x + y )
        start = 1
    #Вычитание
    if (value == 2):
        x = float(input(" Введите первое число: "))
        print (' ----------------------------')
        y = float(input(" Введите второе число: "))
        print (' ----------------------------')
        print (' {} - {}'.format(x, y))   
        print (' ----------------------------')    
        print ( x - y )
        start = 1
    #Деление
    if (value == 3):
        x = float(input(" Введите первое число: "))
        print (' ----------------------------')
        y = float(input(" Введите второе число: "))
        print (' ----------------------------')
        print (' {} / {}'.format(x, y))
        print (' ----------------------------')
        print float( x / y )
        start = 1
    #Умножение
    if (value == 4):
        x = float(input(" Введите первое число: "))
        print (' ----------------------------')
        y = float(input(" Введите второе число: "))
        print (' ----------------------------')
        print (' {} * {}'.format(x, y))
        print (' ----------------------------')
        print ( x * y )
        start = 1
    #Найти синус
    if (value == 5):
        x = float(input(" Введите число: "))
        print (' ----------------------------')
        print float( sin(x) )
        start = 1
    #Найти косинус
    if (value == 6):
        x = float(input(" Введите число: "))
        print (' ----------------------------')
        print float( cos(x) )
        start = 1
    #Найти тангенс
    if (value == 7):
        x = float(input(" Введите число: "))
        print (' ----------------------------')
        print float( tan(x) )
        start = 1
    #Найти котангенс
    if (value == 8):
        x = float(input(" Введите число: "))
        tan = tan(x)
        print (' ----------------------------')
        print float( 1/tan )
        start = 1
    #Строим график
    if (value == 9):

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
    #Производная
    if (value == 10):
        x = sympy.Symbol('x')
        y = sympy.Symbol('y')
        input_string = input('Выражение: ')
        print ("")
        print ("")
        sympy.pprint (sympy.diff(input_string))
    else:
        start = 1
