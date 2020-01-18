# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:41:06 2020
 
@author: Aluno
"""

soma = 0
n = 0
while True:
    x = int(input("digite o numero (0 sai): "))
    if x ==0:
        break
    else:
        n = n + 1
    soma += x
print ("media: %5.2f" %(soma/n))    