#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Импорт библиотек
import scipy, math, cmath, sympy, mpmath, numpy, pandas, matplotlib, sys, matplotlib.pyplot as plt, os

#Импорт из библиотек
from sympy import *
from math import *
from cmath import *
from mpmath import *
from scipy import *
from numpy import *
from pandas import *
from matplotlib import *
from sys import *
from os import *

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
    print ('----------------------------')
    value = int(input(" Выберите нужное действие: \n  \n 1) Сложение  \n 2) Вычитание \n 3) Деление \n 4) Умножение \n 5) Найти синус \n 6) Найти косинус \n 7) Найти тангенс \n 8) Найти котангенс \n 9) Построить график по 2 точкам  \n ---------------------------- \n "))

    #Сложение
    if (value == 1):
        x = float(input(" Введите первое число: "))
        print ('----------------------------')
        y = float(input(" Введите второе число: "))
        print ('----------------------------')
        print ('{} + {}'.format(x, y)) 
        print ('----------------------------')    
        print (x + y)
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1): 
            start = 1
    #Вычитание
    if (value == 2):
        x = float(input(" Введите первое число: "))
        print ('----------------------------')
        y = float(input(" Введите второе число: "))
        print ('----------------------------')
        print ('{} - {}'.format(x, y))   
        print ('----------------------------')    
        print (x - y)
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1):
            start = 1
    #Деление
    if (value == 3):
        x = float(input(" Введите первое число: "))
        print ('----------------------------')
        y = float(input(" Введите второе число: "))
        print ('----------------------------')
        print ('{} / {}'.format(x, y))
        print ('----------------------------')
        print float(x / y)
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1):
            start = 1
    #Умножение
    if (value == 4):
        x = float(input(" Введите первое число: "))
        print ('----------------------------')
        y = float(input(" Введите второе число: "))
        print ('----------------------------')
        print ('{} * {}'.format(x, y))
        print ('----------------------------')
        print (x * y)
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1):
            start = 1
    #Найти синус
    if (value == 5):
        x = float(input(" Введите число: "))
        print ('----------------------------')
        print float(sin(x))
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1):
            start = 1
    #Найти косинус
    if (value == 6):
        x = float(input(" Введите число: "))
        print ('----------------------------')
        print float(cos(x))
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1): 
            start = 1
    #Найти тангенс
    if (value == 7):
        x = float(input(" Введите число: "))
        print ('----------------------------')
        print float(tan(x))
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1): 
            start = 1
    #Найти котангенс
    if (value == 8):
        x = float(input(" Введите число: "))
        tan = tan(x)
        print ('----------------------------')
        print float(1/tan)
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0):
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1):
            start = 1

    if (value == 9):

        fig = plt.figure()

        ax = fig.add_subplot(111)
        rect = ax.patch
        rect.set_facecolor('white')
        rect.set_alpha(0)
        print("")
        x = np.arange(input(" Введите точку x: "))
        y = input(" Введите выражение y: ")

        ax.plot(x, y, 'black')

        xax = ax.xaxis

        xlocs = xax.get_ticklocs()
        xlabels = xax.get_ticklabels()
        xlines = xax.get_ticklines()

        # вспомогательная сетка для главных делений 
        ax.grid(True, which=u'major', color='w', linewidth=2., linestyle='solid')

        # вспомогательная сетка для вспомогательных делений 
        ax.grid(True, which=u'minor', color='w')


        # Ось абсцисс
        for label in ax.xaxis.get_ticklabels():
            # label - это экземпляр текста Text
            label.set_color('black')
            label.set_rotation(-45)
            label.set_fontsize(15)

        # Ось ориднат
        for line in ax.yaxis.get_ticklines():
            # line - это экземпляр плоской линии Line2D
            line.set_color('black')   # задаём цвет линии деления
            line.set_markersize(14)   # задаём длину линии деления
            line.set_markeredgewidth(1.5)   # задаём толщину линии деления

        save('pic_8_1_1', fmt='png')

        for label in xlabels:
            # цвет подписи деленений оси OX
            label.set_color('black')
            # поворот подписей деленений оси OX 
            label.set_rotation(45)
            # размер шрифта подписей делений оси OX 
            label.set_fontsize(12)
            
        plt.show()
        print ('----------------------------')
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 0): # FIXME: Выходит не с первого раза..
            print ('----------------------------')
            print (" Спасибо за использование!")
            print ('----------------------------')
            sys.exit()
        elif (value == 1): 
            start = 1
    else:
        print ('----------------------------')
        value = input(" Вы хотите выйти? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ('----------------------------')
            print (" Спасибо за использование!")
            sys.exit()
        elif (value == 0):
            start = 1