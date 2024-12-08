#!/usr/bin/env python3
import time, locale
name = input('Geben SIe Ihren Namen ein:')
print('Hello %s!' %name)

locale.setlocale(locale.LC_ALL, '')
time =time.strftime('Heute ist %A,der %d. %B.')
print(time)
