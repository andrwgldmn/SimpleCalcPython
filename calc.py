#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Импорт библиотек
import scipy, math, cmath, sympy, mpmath, numpy, pandas, matplotlib, sys

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

#Начало
start = 1
while start:
    start = 0

#Запрос на выбор операций
    print ("")
    value = int(input(" Выберите нужное действие: \n  \n 1) Сложение  \n 2) Вычитание \n 3) Деление \n 4) Умножение \n 5) Найти синус \n 6) Найти косинус \n 7) Найти тангенс \n 8) Найти котангенс \n \n  ")) # 9) Найти производную \n 10) Найти интеграл \n))
    print ("")

    #Сложение
    if (value == 1):
        x = float(input(" Введите первое число: "))
        print ("")
        y = float(input(" Введите второе число: "))
        print ("")
        print ('{} + {}'.format(x, y)) 
        print ("")    
        print (x + y)
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    #Вычитание
    if (value == 2):
        x = float(input(" Введите первое число: "))
        print ("")
        y = float(input(" Введите второе число: "))
        print ("")
        print ('{} - {}'.format(x, y))   
        print ("")    
        print (x - y)
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    #Деление
    if (value == 3):
        x = float(input(" Введите первое число: "))
        print ("")
        y = float(input(" Введите второе число: "))
        print ("")
        print ('{} / {}'.format(x, y))
        print ("")
        print float(x / y)
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    #Умножение
    if (value == 4):
        x = float(input(" Введите первое число: "))
        print ("")
        y = float(input(" Введите второе число: "))
        print ("")
        print ('{} * {}'.format(x, y))
        print ("")
        print (x * y)
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    #Найти синус
    if (value == 5):
        x = float(input(" Введите число: "))
        print ("")
        print float(sin(x))
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    #Найти косинус
    if (value == 6):
        x = float(input(" Введите число: "))
        print ("")
        print float(cos(x))
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    #Найти тангенс
    if (value == 7):
        x = float(input(" Введите число: "))
        print ("")
        print float(tan(x))
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    #Найти котангенс
    if (value == 8):
        x = float(input(" Введите число: "))
        tan = tan(x)
        print ("")
        print float(1/tan)
        print ("")
        value = input(" Вы хотите продолжить? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0): # FIXME: Выходит не с первого раза..
            start = 1
    else:
        print ("")
        value = input(" Вы хотите выйти? \n \n Если да, введите 1. \n \n Если нет, введите 0. \n \n " )
        if (value == 1):
            print ("")
            print ("Спасибо за использование!")
            sys.exit()
        elif (value == 0):
            start = 1