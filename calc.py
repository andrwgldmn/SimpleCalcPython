#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
from sys import exit

value = None
while value != 0:

    value = int(input(" \n 0) Выход/Exit/Вихід \n 1) Русский \n 2) English \n 3) Українська \n \n" ))
    if (value == 0):
        sys.exit()
    elif (value == 1):
        import rus
    elif (value == 2):
        import eng
    elif (value == 3):
        import ukr
    else:
        print("I don't know what you write, try again")
