#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Import libraries
import math, sympy, sympy.abc, numpy as np, matplotlib, sys, matplotlib.pyplot as plt, os, scipy, time

#import from libraries
from sympy import *
from math import sin, cos, tan
from sys import *
from os import *
from sympy.abc import symbols, x, y, theta

#Delay before cleaning
delay = 10            #time of delay in seconds;

#For saving graphic in file
def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)

#Cleaning screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Begin
start = 1
while start:
    start = 0

#Request for selection of operations
    print (' ----------------------------')
    value = int(input(" Select a category: \n \n 0) Exit \n 1) Simple actions \n 2) Trigonometry \n 3) Geometry \n 4) Other \n 5) Higher Mathematics \n 6) Electricity \n ---------------------------- \n "  ))
    #Exit
    if (value == 0):
        print( '-' * 28 + '\n Thanks for using!\n' +  '-' * 28)
        sys.exit()
    ##############################################################################################################################
    #Simple actions
    if (value == 1):
        value = int(input("\n 11) Addiction  \n 21) Subtraction \n 31) Division \n 41) Multiplication \n \n"))
        #Addiction
        if (value == 11):
            print ("")
            x = float(input(" Enter the first number: "))
            print (' ----------------------------')
            y = float(input(" Enter the second number: "))
            print (' ----------------------------')
            print (' {} + {}'.format(x, y)) 
            print (' ----------------------------')    
            print ( x + y )
            time.sleep(delay)
            cls()
            start = 1
        #Subtraction
        if (value == 21):
            print ("")
            x = float(input(" Enter the first number: "))
            print (' ----------------------------')
            y = float(input(" Enter the second number: "))
            print (' ----------------------------')
            print (' {} - {}'.format(x, y))   
            print (' ----------------------------')    
            print ( x - y )
            time.sleep(delay)
            cls()
            start = 1
        #Division
        if (value == 31):
            print ("")
            x = float(input(" Enter the first number: "))
            print (' ----------------------------')
            y = float(input(" Enter the second number: "))
            print (' ----------------------------')
            print (' {} / {}'.format(x, y))
            print (' ----------------------------')
            print float( x / y )
            time.sleep(delay)
            cls()
            start = 1
        #Multiplication
        if (value == 41):
            print ("")
            x = float(input(" Enter the first number: "))
            print (' ----------------------------')
            y = float(input(" Enter the second number: "))
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
    #Trigonometry
    if (value == 2):
        value = int(input("\n 12) Sine  \n 22) Cosine \n 32) Tangent \n 42) Cotangent \n 52) Secant \n 62) Cosecant \n \n"))
        #Sine
        if (value == 12):
            print ("")
            x = float(input(" Enter a number: "))
            print (' ----------------------------')
            print float( sin(x) )
            time.sleep(delay)
            cls()
            start = 1
        #Cosine
        if (value == 22):
            print ("")
            x = float(input(" Enter a number: "))
            print (' ----------------------------')
            print float( cos(x) )
            time.sleep(delay)
            cls()
            start = 1
        #Tangent
        if (value == 32):
            print ("")
            x = float(input(" Enter a number: "))
            print (' ----------------------------')
            print float( tan(x) )
            time.sleep(delay)
            cls()
            start = 1
        #Cotangent
        if (value == 42):
            print ("")
            x = float(input(" Enter a number: "))
            tan = tan(x)
            print (' ----------------------------')
            print float( 1/tan )
            time.sleep(delay)
            cls()
            start = 1
        #Secant
        if (value == 52):
            print ("")
            x = float(input(" Enter a number: "))
            sin = sin(x)
            print (' ----------------------------')
            print float( 1/sin )
            time.sleep(delay)
            cls()
            start = 1
        #Cosecant
        if (value == 62):
            print ("")
            x = float(input(" Enter a number: "))
            cos = cos(x)
            print (' ----------------------------')
            print float( 1/cos )
            time.sleep(delay)
            cls()
            start = 1
        else:
            start = 1
    ##############################################################################################################################
    #Geometry
    if (value == 3):
        value = int(input("\n 13) Hypotenuse  \n 23) Сathetus \n 33) Area of a Rectangle \n 43) Area of a Triangle \n 53) Area of a Right Triangle-Angled \n 63) Area of a Equilateral Triangle \n 73) Area of a Rhombus \n 83) Area of a Parallelogram \n 93) Area of a Trapezoid \n \n"))
        #Hypotenuse
        if (value == 13):
            print ("")
            katet_one = float(input(" Enter the first сathetus: "))
            katet_two = float(input(" Enter the second сathetus: "))
            gipot = math.sqrt(katet_one**2 + katet_two**2)
            print ("")
            print (gipot)
            time.sleep(delay)
            cls()
            start = 1
        #Сathetus
        if (value == 23):
            print ("")
            katet = float(input(" Enter the cathetus: "))
            gipot = float(input(" Enter the hypotenuse : "))
            res = math.sqrt(gipot**2 - katet**2)
            print ("")
            print (res)
            time.sleep(delay)
            cls()
            start = 1
        #Area of a Rectangle
        if (value == 33):
            print ("")
            one = float(input(" Enter the first side: "))
            two = float(input(" Enter the second side: ")) 
            print ("")
            print (two * one)
            time.sleep(delay)
            cls()
            start = 1
        #Area of a Triangle
        if (value == 43):
            print ("")
            one = float(input(" Enter the side: "))
            two = float(input(" Enter the height: ")) 
            print ("")
            print ((one*two)*0.5)
            time.sleep(delay)
            cls()
            start = 1
        #Area of a Right-Angled Ariangle
        if (value == 53):
            print ("")
            one = float(input(" Enter the first side: "))
            two = float(input(" Enter the second side: ")) 
            print ("")
            print ((one*two)/2)
            time.sleep(delay)
            cls()
            start = 1
        #Area of a Equilateral Triangle
        if (value == 63):
            print ("")
            three = 3
            one = float(input(" Enter the side: "))
            print ("")
            print ((one*math.sqrt(three))/4)
            time.sleep(delay)
            cls()
            start = 1
        #Area of a Rhombus
        if (value == 73):
            print ("")
            one = float(input(" Enter the side: "))
            two = float(input(" Enter the height: ")) 
            print ("")
            print (one * vis)
            time.sleep(delay)
            cls()
            start = 1
        #Area of a Parallelogram
        if (value == 83):
            print ("")
            one = float(input(" Enter the first side: "))
            two = float(input(" Enter the second side: "))
            sine = float(input(" Enter an angle: "))
            print ("")
            print (one * two * math.sin(sine))
            time.sleep(delay)
            cls()
            start = 1
        #Area of a Trapezoid
        if (value == 93):
            print ("")
            one = float(input(" Enter the first side: "))
            two = float(input(" Enter the second side: "))
            two = float(input(" Enter the height: ")) 
            print ("")
            print (((one + two)/2)*vis)
            time.sleep(delay)
            cls()
            start = 1
        else:
            start = 1
    ##############################################################################################################################
    #Other
    if (value == 4):
        value = int(input("\n 14) Graphic  \n 24) Simplify \n \n "))
        #Graphic
        if (value == 14):
            fig = plt.figure()
            #Type of graphic
            ax = fig.add_subplot(111)
            rect = ax.patch
            rect.set_facecolor('white')
            rect.set_alpha(0)
            print("")
            #Limit by х
            x = np.arange(-25, 25)
            #Enter
            y = input(" Enter the math.example: ")
            plt.plot(x, y)
            ax = plt.gca()
            ax.plot(x, y, 'black')
            xax = ax.xaxis
            xlocs = xax.get_ticklocs()
            xlabels = xax.get_ticklabels()
            xlines = xax.get_ticklines()
            ax.grid(True, which='major', color='y', linewidth=2., linestyle='solid')
            ax.grid(True, which='minor', color='k')
            for label in ax.xaxis.get_ticklabels():
                label.set_color('black')
                label.set_rotation(0)
                label.set_fontsize(14)
            for line in ax.yaxis.get_ticklines():
                line.set_color('black')   
                line.set_markersize(14)   
                line.set_markeredgewidth(3)   
            #Saving to the file 
            save('graphic', fmt='png')
            for label in xlabels:
                label.set_color('black')
                label.set_rotation(0)
                label.set_fontsize(12)
            #Show a graphic
            plt.show()
            start = 1
        else:
            start = 1
            #Simplify
            if (value == 24):
                print ("")
                primer = raw_input(" Enter the math.example: ")
                res = simplify(primer)
                print ("")
                sympy.pprint (res)
                time.sleep(delay)
                cls()
                start = 1
            else:
                start = 1
    ##############################################################################################################################
    #Higher Mathematics
    if (value == 5):
        value = int(input("\n 15) Derivative  \n 25) Integral \n 35) Limit (x->оо) \n 45) Limit (x->0) \n 55) Limit (x->1) \n 65) Limit (any number) \n 75) Definite Integral \n \n "))
        #Derivative
        if (value == 15):
            print ("")
            input_string = raw_input(' Enter the math.example: ')
            print ("")
            res = sum(sympy.diff(input_string, var) for var in [x,y])
            sympy.pprint (res)
            time.sleep(delay)
            cls()
            start = 1
        #Integral
        if (value == 25):
            print ("")
            input_string = raw_input(' Enter the math.example: ')
            print ("")
            sympy.pprint (sympy.Integral(input_string, x))
            print ("")
            sympy.pprint (integrate(input_string, x))
            time.sleep(delay)
            cls()
            start = 1
        #Definite Integral
        if (value == 75):
            print ("")
            input_string = raw_input(' Enter the math.example: ')
            ot = float(input(' From: '))
            do = float(input(' To: '))
            print ("")
            sympy.pprint (sympy.Integral(input_string, (x, ot, do)))
            print ("")
            sympy.pprint (integrate(input_string, (x, ot, do)))
            time.sleep(delay)
            cls()
            start = 1
        #Limit (x->оо)
        if (value == 35 ):
            print ("")
            value = input(' Enter the math.example: ') 
            print ("")
            sympy.pprint (limit(value, x, oo))
            time.sleep(delay)
            cls()
            start = 1
        #Limit (x->0)
        if (value == 45 ):
            print ("")
            value = input(' Enter the math.example: ') 
            print ("")
            sympy.pprint (limit(value, x, 0))
            time.sleep(delay)
            cls()
            start = 1
        #Limit (x->1)
        if (value == 55 ):
            print ("")
            value = input(' Enter the math.example: ') 
            print ("")
            sympy.pprint (limit(value, x, 1))
            time.sleep(delay)
            cls()
            start = 1
        #Limit (any numbers)
        if (value == 65 ):
            print ("")
            value = input(' Enter the math.example: ') 
            stremlenie = input(' What "x" tends to? ')
            print ("")
            sympy.pprint (limit(value, x, stremlenie))
            time.sleep(delay)
            cls()
            start = 1 
        else:
            start = 1
    ################################################################################################################################
    if (value == 6):
        value = int(input("\n 16) Active Resistance  \n 26) Inductive Resistance \n 36) Capacitance \n 46) Power \n 56) Current \n 66) Voltage \n \n "))
        #Active Resistance
        if (value == 16):
            print ("")
            u = float(input(" Voltage: "))
            print (' ----------------------------')
            i = float(input(" Current: "))  
            print ("")
            print ( u/i )
            time.sleep(delay)
            cls()
            start = 1 
        #Inductive Resistance
        if (value == 26):
            print ("")
            l = float(input(" Inductance: "))
            print (' ----------------------------')
            f = float(input(" Frequency: "))  
            print ("")
            print ( 2*math.pi*f*l )
            time.sleep(delay)
            cls()
            start = 1 
        #Capacitance
        if (value == 36):
            print ("")
            c = float(input(" Capacity: "))
            print (' ----------------------------')
            f = float(input(" Frequency: ")) 
            print ("") 
            print ( 1/(2*math.pi*f*c) )
            time.sleep(delay)
            cls()
            start = 1
        #Power
        if (value == 46):
            print ("")
            u = float(input(" Voltage: "))
            print (' ----------------------------')
            i = float(input(" Current: ")) 
            print ("") 
            print ( u*i )
            time.sleep(delay)
            cls()
            start = 1 
        #Current
        if (value == 56):
            print ("")
            u = float(input(" Voltage: "))
            print (' ----------------------------')
            r = float(input(" Resistance: ")) 
            print ("") 
            print ( u/r )
            time.sleep(delay)
            cls()
            start = 1 
        #Voltage
        if (value == 66):
            print ("")
            r = float(input(" Resistance: "))
            print (' ----------------------------')
            i = float(input(" Current: ")) 
            print ("") 
            print ( r*i )
            time.sleep(delay)
            cls()
            start = 1 
    else:
       start = 1
