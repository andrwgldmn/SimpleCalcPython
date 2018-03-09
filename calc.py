#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Импорт библиотек
import scipy, sys, math, cmath, itertools, sympy, mpmath, numpy

#Импорт из библиотек
from sympy import *
from math import *
from cmath import *
from itertools import *
from mpmath import *
from sys import *
from scipy import *
from numpy import *

#Запрос на выбор операций
print ("")
value = int(input("Выберите нужное действие: \n  \n 1) Сложение  \n 2) Вычитание \n 3) Деление \n 4) Умножение \n 5) Найти синус \n 6) Найти косинус \n 7) Найти тангенс \n 8) Найти котангенс \n  "))
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

#Найти тангенс
if (value == 8):
    x = float(input("Введите число: "))
    sin = sin(x)
    cos = cos(x)
    print ("")
    print float(cos/sin)