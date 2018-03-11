#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
from sys import exit

start = 1
while start:
    start = 0

    value = int(input(" \n 0) Выход/Exit/Вихід \n 1) Русский \n 2) English \n 3) Українська \n \n" ))
    if (value == 0):
        sys.exit()
    if (value == 1):
        import rus
    if (value == 2):
        import eng
    if (value == 3):
        import ukr
    else:
        start = 1