#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
from sys import exit

value = None
while value != 0:

    value = int(input(" \n 0) Выход/Exit/Вихід \n 1) English \n 3) Українська \n \n" ))
    if (value == 0):
        sys.exit()
    elif (value == 1):
        import eng
    elif (value == 2):
        import ukr
    else:
        print("I don't know what you write, try again")
