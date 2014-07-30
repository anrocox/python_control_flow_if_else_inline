#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

In Python, how to define an if-else in a single line of code?

En Python, ¿Cómo definir un if-else en una sola linea de código?
'''

#statement_true  if  expression  else  statement_false
#the expression is evaluated, then either statement_true or statement_false is
#returned based on the boolean value of expression

#create a integer
n = 100
print(n)

#if n is greater than 100, n is multiplied by 5, otherwise n is divided by 5
new = n * 5 if n > 50 else n / 5
print(new)
