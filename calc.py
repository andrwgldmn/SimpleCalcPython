#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

start = 1
while start:
    start = 0

value = int(input(" \n 1) Русский \n 2) English \n 3) Українська \n \n" ))
if (value == 1):
    import rus
if (value == 2):
    import eng
if (value == 3):
    import ukr
else:
    start()