#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Импорт библиотек
import scipy, math, cmath, sympy, mpmath, numpy, pandas, matplotlib

#Импорт из библиотек
from sympy import *
from math import *
from cmath import *
from mpmath import *
from scipy import *
from numpy import *
from pandas import *
from matplotlib import *

#Начало
start = 1
while start:
    start = 0

#Запрос на выбор операций
    print ("")
    value = int(input("Выберите нужное действие: \n  \n 1) Сложение  \n 2) Вычитание \n 3) Деление \n 4) Умножение \n 5) Найти синус \n 6) Найти косинус \n 7) Найти тангенс \n 8) Найти котангенс \n 9) Найти производную \n 10) Найти интеграл \n \n  "))
    print ("")

    #Сложение
    if (value == 1):
        x = float(input("Введите первое число: "))
        print ("")
        y = float(input("Введите второе число: "))
        print ("")
        print ('{} + {}'.format(x, y)) 
        print ("")    
        print (x + y)

    #Вычитание
    if (value == 2):
        x = float(input("Введите первое число: "))
        print ("")
        y = float(input("Введите второе число: "))
        print ("")
        print ('{} - {}'.format(x, y))   
        print ("")    
        print (x - y)

    #Деление
    if (value == 3):
        x = float(input("Введите первое число: "))
        print ("")
        y = float(input("Введите второе число: "))
        print ("")
        print ('{} / {}'.format(x, y))
        print ("")
        print float(x / y)

    #Умножение
    if (value == 4):
        x = float(input("Введите первое число: "))
        print ("")
        y = float(input("Введите второе число: "))
        print ("")
        print ('{} * {}'.format(x, y))
        print ("")
        print (x * y)

    #Найти синус
    if (value == 5):
        x = float(input("Введите число: "))
        print ("")
        print float(sin(x))

    #Найти косинус
    if (value == 6):
        x = float(input("Введите число: "))
        print ("")
        print float(cos(x))

    #Найти тангенс
    if (value == 7):
        x = float(input("Введите число: "))
        print ("")
        print float(tan(x))

    #Найти котангенс
    if (value == 8):
        x = float(input("Введите число: "))
        tan = tan(x)
        print ("")
        print float(1/tan)
#FIXME
    #Найти производную:
    if (value == 9):
        print("Введите выражение: ")
        print ("")
        x = Symbol("x")
        y = y.diff(x)
        print ("")
        print ("y")
    start = 1